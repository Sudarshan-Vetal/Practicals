#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np
import matplotlib.pyplot as plt


# In[45]:


def func(x):
    return (x+3)**2


# In[46]:


def gradient(x):
    return 2*(x+3)


# In[58]:


start = 2
learning_rate = 0.2
iterations = 50


# In[59]:


x_history = [start]
y_history = [func(start)]


# In[60]:


def gradient_descent(start, learning_rate, iterations):
    x = start
    for i in range(iterations):
        gradient_val = gradient(x)
        x = x - learning_rate * gradient_val
        x_history.append(x)
        y_history.append(func(x))


# In[61]:


gradient_descent(start, learning_rate, iterations)


# In[62]:


x_values = np.linspace(-10,4,400)
y_values = func(x_values)


# In[63]:


plt.figure(figsize=(10,6))
plt.plot(x_values, y_values, label ="y=(x+3)**2")
plt.scatter(x_history,y_history, color='red',label="Gradient Descent Path")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid('True')
plt.title("Gradient Descent Optimization of y=(x+3)**2")
plt.show()

print("Local Minimum at x = ", x_history[-1])
print("Minimum value of y = ", y_history[-1])

