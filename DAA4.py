#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


# In[12]:


def dynamic_knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for r in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], items[i - 1].profit + dp[i - 1][w - items[i - 1].weight])
            else:
                dp[i][w] = dp[i - 1][w]
    
    for i in range(n+1):
        for w in range(capacity+1):
            print(dp[i][w],end=" ")
            
        print("")
    return dp[n][capacity]


# In[13]:


def branch_and_bound_knapsack(items, capacity):
    n = len(items)
    best_profit = 0

    def bound(i, w, p):
        bound = p
        while i < n and w + items[i].weight <= capacity:
            w = w + items[i].weight
            bound = bound + items[i].profit
            i = i + 1
        if i < n:
            bound = bound + (capacity - w) * (items[i].profit / items[i].weight)
        return bound

    def knapsack_recursive(i, w, p):
        nonlocal best_profit
        if i == n or w == capacity:
            if p > best_profit:
                best_profit = p
            return
        if w + items[i].weight <= capacity:
            knapsack_recursive(i + 1, w + items[i].weight, p + items[i].profit)
        if bound(i + 1, w, p) > best_profit:
            knapsack_recursive(i + 1, w, p)

    knapsack_recursive(0, 0, 0)
    return best_profit


# In[14]:


n = int(input("Enter the number of items: "))
items = []
for i in range(n):
    profit = int(input("Enter the profit: "))
    weight = int(input("Enter the weight: "))
    items.append(Item(profit, weight))
capacity = int(input("Enter the capacity of Knapsack: "))

while True:
    print("\n0-1 Knapsack Problem Solver")
    print("1. Dynamic Programming")
    print("2. Branch and Bound")
    print("3. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = dynamic_knapsack(items, capacity)
        print("Total profit using Dynamic Programming:", result)
    elif choice == 2:
        result = branch_and_bound_knapsack(items, capacity)
        print("Total profit using Branch and Bound:", result)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")

