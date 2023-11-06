#!/usr/bin/env python
# coding: utf-8

# In[1]:


import timeit


# In[2]:


def fibonacci_iterative(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        a,b = 0,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b


# In[3]:


def fibonacci_recursive(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


# In[4]:


FibArray = [0,1]
def fibonacci_dp(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    elif n < len(FibArray):
        return FibArray[n]
    else:
        res = fibonacci_dp(n-1)+fibonacci_dp(n-2)
        FibArray.append(res)
        return FibArray[n]


# In[5]:


while True:
    print("\nFIBONACCI NUMBER CALCULATOR")
    print("1. Iterative Approach")
    print("2. Recursive Approach")
    print("3. Dynamic Programming Approach")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice==1:
        n=int(input("Enter value of n : "))
        start_time = timeit.default_timer()
        result = fibonacci_iterative(n)
        end_time = timeit.default_timer()
        print("\nFibonacci ",n," by Iterative Approach : ",result)
        print("Execution Time   : ",end_time-start_time," seconds")
        print("Time Complexity  : O(n)")
        print("Space Complexity : O(1)")

    elif choice==2:
        n=int(input("Enter value of n : "))
        start_time = timeit.default_timer()
        result = fibonacci_recursive(n)
        end_time = timeit.default_timer()
        print("\nFibonacci ",n," by Recursive Approach : ",result)
        print("Execution Time   : ",end_time-start_time," seconds")
        print("Time Complexity  : O(2^n)")
        print("Space Complexity : O(n)")

    elif choice==3:
        n=int(input("Enter value of n : "))
        start_time = timeit.default_timer()
        result = fibonacci_dp(n)
        end_time = timeit.default_timer()
        print("\nFibonacci ",n," by DP Approach : ",result)
        print("Execution Time   : ",end_time-start_time," seconds")
        print("Time Complexity  : O(n)")
        print("Space Complexity : O(n)")

    elif choice==4:
        print("\nExiting...............")
        break

    else:
        print("\nInvalid Input")

