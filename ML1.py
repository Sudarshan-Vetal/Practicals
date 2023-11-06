#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[14]:


import numpy as np
import pandas as pd


# In[16]:


df = pd.read_csv('uber.csv')


# In[17]:


df


# In[18]:


df.size


# In[19]:


df.info()


# In[20]:


df.describe()


# In[21]:


df.head()


# In[22]:


df = df.drop(['Unnamed: 0','key'], axis=1)


# In[23]:


df


# In[27]:


df.isnull().sum()


# In[28]:


df.dropna(axis=0, inplace=True)


# In[29]:


df


# In[30]:


df.isnull().sum()


# In[31]:


df.dtypes


# In[33]:


df.pickup_datetime = pd.to_datetime(df.pickup_datetime, errors='coerce')


# In[34]:


df = df.assign(
    second = df.pickup_datetime.dt.second,
    minute = df.pickup_datetime.dt.minute,
    hour = df.pickup_datetime.dt.hour,
    day = df.pickup_datetime.dt.day,
    month = df.pickup_datetime.dt.month,
    year = df.pickup_datetime.dt.year,
    dayofweek = df.pickup_datetime.dt.dayofweek
)


# In[38]:


df = df.drop('pickup_datetime',axis=1)


# In[39]:


df


# In[40]:


df.info()


# In[41]:


df.head()


# In[44]:


incorrect_coordinates = df.loc[
    (df.pickup_longitude>180) | (df.pickup_longitude<-180)|
    (df.dropoff_longitude>90) | (df.dropoff_longitude<-90)|
    (df.dropoff_latitude>90)  | (df.dropoff_latitude<-90) |
    (df.pickup_latitude>90)   | (df.pickup_latitude<-90)
]


# In[45]:


df.drop(incorrect_coordinates, inplace=True, errors='ignore')


# In[46]:


df


# In[47]:


def distance_transform(longitude1, latitude1, longitude2, latitude2):
    long1, lati1, long2, lati2 = map(np.radians, [longitude1, latitude1, longitude2, latitude2])
    dist_long = long2-long1
    dist_lati = lati2-lati1
    a = np.sin(dist_lati/2)**2 + np.cos(lati1) * np.cos(lati2) * np.sin(dist_long/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) * 6371
    
    return c


# In[48]:


df['Distance'] = distance_transform(
    df['pickup_longitude'],
    df['pickup_latitude'],
    df['dropoff_longitude'],
    df['dropoff_latitude']
)


# In[49]:


df


# In[50]:


import matplotlib.pyplot as plt


# In[53]:


plt.figure(figsize=(20,12))
plt.scatter(df['Distance'], df['fare_amount'])


# In[54]:


plt.figure(figsize=(20,12))
import seaborn as sns

sns.boxplot(data=df)


# In[56]:


df.drop(df[df['Distance']>=60].index , inplace = True)
df.drop(df[df['fare_amount']<=0].index, inplace = True)

df.drop(df[(df['fare_amount']>100) & (df['Distance']<1)].index, inplace=True)
df.drop(df[(df['fare_amount']<100) & (df['Distance']>100)].index, inplace=True)


# In[57]:


df


# In[58]:


plt.scatter(df['Distance'],df['fare_amount'])


# In[59]:


corr = df.corr()


# In[60]:


corr.style.background_gradient()


# In[61]:


X = df['Distance'].values.reshape(-1,1)


# In[62]:


y = df['fare_amount'].values.reshape(-1,1)


# In[63]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)


# In[64]:


print(X_std)
print(y_std)


# In[65]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_std, y_std, test_size=0.2, random_state=0)


# In[66]:


from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)


# In[67]:


y_pred = lr.predict(X_test)


# In[69]:


y_test = y_test.ravel()


# In[70]:


y_test


# In[71]:


result = pd.DataFrame()
result['Actual']=y_test
result['Predicted']=y_pred


# In[72]:


result


# In[73]:


from sklearn.metrics import mean_squared_error, r2_score

print('RMSE : ',np.sqrt(mean_squared_error(y_test, y_pred)))
print('R2   : ',r2_score(y_test, y_pred))


# In[76]:


plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train,lr.predict(X_train), color='red')


# In[77]:


plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test,lr.predict(X_test), color='red')


# In[78]:


from sklearn.ensemble import RandomForestRegressor


# In[80]:


rfr = RandomForestRegressor(n_estimators = 100, random_state=10)


# In[81]:


rfr.fit(X_train,y_train)


# In[82]:


rfr_pred = rfr.predict(X_test)


# In[83]:


result2 = pd.DataFrame()
y_test = y_test.ravel()


# In[84]:


result2['Actual']=y_test


# In[85]:


result2['Predicted']=rfr_pred


# In[86]:


result2


# In[87]:


print('RMSE : ',np.sqrt(mean_squared_error(y_test, rfr_pred)))
print('R2   : ',r2_score(y_test, rfr_pred))


# In[89]:


plt.scatter(X_test, y_test, color='blue')
plt.scatter(X_test, rfr_pred, color='red')


# In[90]:


table = pd.DataFrame(columns = ['Model','RMSE','R2_SCORE'])


# In[93]:


new_data1 = {
    'Model': 'Linear Regression',
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
    'R2_SCORE':r2_score(y_test, y_pred)
}

table = table.append(new_data1, ignore_index=True)


# In[94]:


new_data2 = {
    'Model': 'Random Forest Regression',
    'RMSE': np.sqrt(mean_squared_error(y_test, rfr_pred)),
    'R2_SCORE':r2_score(y_test, rfr_pred)
}

table = table.append(new_data2, ignore_index=True)


# In[95]:


table

