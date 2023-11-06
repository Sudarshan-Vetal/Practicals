#!/usr/bin/env python
# coding: utf-8

# In[90]:


import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# In[91]:


df = pd.read_csv('diabetes.csv')


# In[92]:


df


# In[93]:


df.shape


# In[94]:


df.size


# In[95]:


df.info()


# In[96]:


df.describe()


# In[97]:


df.isnull().sum()


# In[98]:


df.head()


# In[99]:


df.corr().style.background_gradient()


# In[100]:


df.drop(['BloodPressure','SkinThickness'], axis=1, inplace=True)


# In[101]:


df.head()


# In[102]:


hist = df.hist(figsize=(16,9))


# In[103]:


X = df.iloc[:,:-1]
y = df.iloc[:,-1]


# In[104]:


from sklearn.model_selection import train_test_split


# In[105]:


X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=8)


# In[106]:


from sklearn.preprocessing import StandardScaler


# In[107]:


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)


# In[108]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


# In[109]:


param_grid = {'n_neighbors':range(1,51)}


# In[110]:


model = KNeighborsClassifier()


# In[111]:


grid_search = GridSearchCV(model, param_grid,cv=5)


# In[112]:


grid_search.fit(X_train,y_train)


# In[113]:


best_n_neighbors = grid_search.best_params_['n_neighbors']


# In[114]:


y_pred = grid_search.predict(X_test)


# In[115]:


y_pred


# In[116]:


table = pd.DataFrame()
table['Actual'] = y_test
table['Predicted'] = y_pred


# In[117]:


table


# In[119]:


from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score


# In[121]:


accuracy = accuracy_score(y_test,y_pred)
error = 1-accuracy
recall= recall_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)


# In[122]:


cm=confusion_matrix(y_test,y_pred)


# In[123]:


accuracy


# In[124]:


error


# In[125]:


precision


# In[126]:


recall


# In[127]:


cm


# In[131]:


from sklearn.metrics import classification_report
cr = classification_report(y_test,y_pred)


# In[133]:


print(cr)

