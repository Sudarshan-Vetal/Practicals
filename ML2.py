#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('emails.csv')


# In[3]:


df


# In[4]:


df.size


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.head()


# In[8]:


df.isnull().sum()


# In[9]:


X = df.iloc[:,1:-1]
y = df.iloc[:,-1]


# In[10]:


X.shape


# In[11]:


y.shape


# In[12]:


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.25, random_state=8)


# In[13]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import accuracy_score


# In[14]:


models = {
    "K-Nearest Neighbours": KNeighborsClassifier(n_neighbors=2),
    "Linear SVM": LinearSVC(random_state=8, max_iter=1000),
    "Polynomial SVM": SVC(kernel="poly",degree=2, random_state=8),
    "RBF SVM": SVC(kernel='rbf',random_state=8),
    "Sigmoid SVM": SVC(kernel='sigmoid',random_state=8)
}


# In[15]:


from sklearn.metrics import confusion_matrix


# In[16]:


for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\nMODEL : ",model_name)
    print("Accuracy : ",accuracy_score(y_test,y_pred))
    cm = confusion_matrix(y_test,y_pred)
    print("Confusion Matrix\n",cm)

