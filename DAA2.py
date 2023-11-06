#!/usr/bin/env python
# coding: utf-8

# In[2]:


import heapq


# In[3]:


class Node:
    def __init__(self, freq, symbol,left=None,right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
        
    def __lt__(self, nxt):
        return self.freq < nxt.freq


# In[4]:


def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(node.symbol," -> ",newVal)


# In[6]:


n = int(input("Enter the number of characters : "))
chars = []
freq  = []
for i in range(n):
    character = str(input("Enter character : "))
    frequency = int(input("Enter frequency : "))
    chars.append(character)
    freq.append(frequency)
    
nodes = []
for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x],chars[x]))
    
while len(nodes)>1:NB   
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff=0
    right.huff=1
    newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(nodes, newNode)

print("HUFFMAN ENCODING")
printNodes(nodes[0])

