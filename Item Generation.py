#!/usr/bin/env python
# coding: utf-8

# In[24]:


## Loading similarity pairing
import pandas as pd

df = pd.read_excel(r'C:\Users\dinos\Desktop\Python Project\Similarity Rating.xlsx')
print(df)


# In[25]:


## Creating historgram for rating distribution
import matplotlib.pyplot as plt

n, bins, patches = plt.hist(x=df, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Histogram of similarity rating')
maxfreq = n.max()


# In[27]:


## Finding quantile for buckets with 10 interval
import numpy as np

print("10th percentile of df is:",np.percentile(df, 10))
print("20th percentile of df is:",np.percentile(df, 20))
print("30th percentile of df is:",np.percentile(df, 30))
print("40th percentile of df is:",np.percentile(df, 40))
print("50th percentile of df is:",np.percentile(df, 50))
print("60th percentile of df is:",np.percentile(df, 60))
print("70th percentile of df is:",np.percentile(df, 70))
print("80th percentile of df is:",np.percentile(df, 80))
print("90th percentile of df is:",np.percentile(df, 90))


# In[34]:


## Similarity pairs list from rating 1 to 5 (1 = low similarity, 5 = high simialirty)
## See (Boles & Clifford, 1989) for more information on similarity matrix 
## Bucket according to percentile
pairs_10 = [["i", "b"], ["i", "e"], ["k", "a"], ["l", "a"], ["l", "c"], 
           ["l", "e"], ["m", "j"], ["m", 'l'], ["n", "k"], ["n", "l"],
           ["o", "f"], ["o", "k"], ["o", "l"], ["p", "l"], ["q", "i"], 
           ["r", "l"], ["s", "h"], ["s", "k"], ["s", "l"], ["v",  "l"],
           ["w", "b"], ["w", "d"], ["w", "l"], ["w", "o"], ["x", "b"], 
           ["x", "d"], ["x", "f"], ["x", "l"], ["x", "o"], ["x", "p"]
           ["y", "l"], ["z", "d"], ["z", "l"]]


# In[36]:


import string
import random


## Create random generator with beginning placement 
result = []

def id_generator_beginning(size = 5, pairs = pairs_10, chars = string.ascii_lowercase):
        for pair in pairs:
            pre_generator = ''.join(random.choice(chars) for _ in range(size - 1))
            pair_list = []
            for letter in pair:
                pair_list.append(letter + pre_generator)
            result.append(pair_list)
        return result
        
id_generator_beginning()


# In[37]:


## Create random generator with end placement 
result = []

def id_generator_end(size = 5, pairs = pairs_10, chars = string.ascii_lowercase):
    for pair in pairs:
        pre_generator = ''.join(random.choice(chars) for _ in range(size - 1))
        pair_list = []
        for letter in pair:
            pair_list.append(pre_generator + letter)
        result.append(pair_list)
    return result
        
id_generator_end()


# In[39]:


## Create random generator with middle placement 
result = []

def id_generator_middle(size = 5, pairs = pairs_10, chars = string.ascii_lowercase):
    for pair in pairs:
        pre_generator = ''.join(random.choice(chars) for _ in range(size - 1))
        pair_list = []
        for letter in pair:
            output = pre_generator[:2] + letter + pre_generator[2:]
            pair_list.append(output)
        result.append(pair_list)
    return result
        
id_generator_middle()


# In[41]:


# Create random generator 
result = []

def id_generator(size = 5, iteration = 10, chars = string.ascii_lowercase):
    for n in range(1, iteration):
        pair = []
        pre_generator = ''.join(random.choice(chars) for _ in range(size))
        pair.append(pre_generator)
        pair.append(pre_generator)
        result.append(pair)
    return result
        
    
id_generator(iteration = 20)


# In[ ]:


## Next step

