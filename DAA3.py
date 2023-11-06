#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Item:
    def __init__(self, profit,weight):
        self.profit=profit
        self.weight=weight


# In[6]:


def fractionalKnapsack(W,arr):
    arr.sort(key=lambda x:(x.profit)/(x.weight),reverse=True)
    finalprofit = 0
    
    for item in arr:
        if item.weight <=W:
            W = W - item.weight
            finalprofit = finalprofit + item.profit
        else:
            finalprofit = finalprofit + item.profit * W/item.weight
            break
    return finalprofit


# In[7]:


W = int(input("Enter the capacity of the Knapsack : "))
n = int(input("Enter the number of items : "))
arr=[]
for i in range(n):
    profit = int(input(f"Enter Profit for Item {i+1} : "))
    weight = int(input(f"Enter Weight for Item {i+1} : "))
    arr.append(Item(profit,weight))
    
max_val = fractionalKnapsack(W,arr)
print("The maximum profit is : ", max_val)

