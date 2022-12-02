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
           ["x", "d"], ["x", "f"], ["x", "l"], ["x", "o"], ["x", "p"],
           ["y", "l"], ["z", "d"], ["z", "l"]]
pairs_20 = [["f", "c"], ["i", "c"], ["j", "a"], ["j", "b"], ["j", "e"],
           ["k", "e"], ["k", "f"], ["k", "i"], ["k", "j"], ["l", "g"],
           ["m", "b"], ["m", "k"], ["q", "k"], ["q", "m"], ["t", "a"],
           ["t", "e"], ["t", "o"], ["t", "q"], ["u", "f"], ["u", "l"],
           ["v", "a"], ["w", "e"], ["w", "f"], ["w", "g"], ["w", "h"],
           ["w", "i"], ["w", "j"], ["w", "k"], ["w", "t"], ["x", "g"],
           ["x", "h"], ["x", "i"], ["x", "j"], ["x", "n"], ["z", "b"],
           ["z", "f"], ["z", "g"], ["z", "o"], ["z", "q"]]
pairs_30 = [["f", "b"], ["h", "a"], ["i", "a"], ["i", "d"], ["i", "h"],
           ["k", "c"], ["m", "d"], ["m", "f"], ["p", "f"], ["q", "f"], 
           ["q", "j"], ["q", "l"], ["v", "i"], ["v", "p"], ["w", "q"],
           ["w", "r"], ["x", "q"], ["x", "t"], ["y", "f"], ["y", "i"],
           ["z", "h"], ["z", "i"], ["z", "j"]]
pairs_40 = [["h", "g"], ["i", "f"], ["i", "g"], ["k", "g"], ["n", "f"],
            ["o", "i"], ["p", "i"], ["p", "m"], ["r", "k"], ["s", "f"],
            ["s", "i"], ["s", "j"], ["s", "q"], ["t", "m"], ["t", "n"],
            ["t", "s"], ["u", "k"], ["u", "t"], ["v", "b"], ["v", "d"],
            ["v", "e"], ["v", "f"], ["v", "g"], ["v", "m"], ["v", "q"],
            ["w", "a"], ["x", "a"], ["x", "w"], ["y", "a"], ["y", "t"],
            ["z", "k"]]
pairs_50 = [["f", "a"], ["f", "d"], ["h", "e"], ["h", "f"], ["l", "h"],
            ["m", "e"], ["m", "i"], ["n", "d"], ["n", "g"], ["n", "i"],
            ["o", "h"], ["o", "j"], ["p", "k"], ["r", "i"], ["s", "b"],
            ["s", "d"], ["s", "n"], ["t", "c"], ["t", "g"], ["t", "h"],
            ["t", "p"], ["u", "i"], ["u", "p"], ["u", "s"], ["v", "s"],
            ["w", "p"], ["x", "c"], ["x", "e"], ["y", "m"], ["y", "o"],
            ["y", "x"], ["z", "p"], ["z", "t"]]
pairs_60 = [["f", "e"], ["j", "c"], ["j", "d"], ["j", "h"], ["k", "d"],
            ["l", "b"], ["l", "d"], ["l", "k"], ["m", "c"], ["m", "g"],
            ["n", "b"], ["n", "j"], ["p", "n"], ["q", "h"], ["q", "n"],
            ["r", "g"], ["r", "q"], ["s", "m"], ["s", "o"], ["s", "r"],
            ["t", "k"], ["u", "b"], ["u", "g"], ["u", "q"], ["v", "k"],
            ["v", "t"], ["w", "c"], ["x", "m"], ["x", "s"], ["x", "u"],
            ["y", "r"], ["z", "n"], ["z", "v"], ["z", "y"]]
pairs_70 = [["d", "a"], ["d", "c"], ["e", "d"], ["g", "f"], ["l", "j"],
            ["m", "a"], ["m", "h"], ["n", "a"], ["n", "e"], ["o", "m"],
            ["p", "j"], ["q", "e"], ["r", "b"], ["r", "o"], ["s", "g"], 
            ["t", "b"], ["t", "d"], ["t", "i"], ["t", "r"], ["u", "d"],
            ["u", "m"], ["v", "r"], ["x", "r"], ["y", "b"], ["y", "c"],
            ["y", "d"], ["y", "j"], ["y", "k"], ["y", "n"], ["z", "m"], 
            ["z", "u"]]
pairs_80 = [["b", "a"], ["c","a"], ["h", "c"], ["k", "b"], ["l", "f"],
            ["o", "g"], ["o", "n"], ["p", "a"], ["p", "c"], ["p", "h"],
            ["q", "a"], ["q", "c"], ["q", "o"], ["r", "a"], ["r", "d"],
            ["r", "f"], ["r", "j"], ["s", "a"], ["s", "p"], ["u", "a"], 
            ["u", "j"], ["v", "h"], ["v", "j"], ["v", "n"], ["w", "n"],
            ["w", "s"], ["y", "h"], ["y", "p"], ["y", "w"], ["z", "a"], 
            ["z", "c"], ["z", "x"]]
pairs_90 = [["c", "b"], ["e", "b"], ["e", "c"], ["g", "a"], ["g", "b"], 
            ["g", "c"], ["g", "e"], ["h", "d"], ["j", "f"], ["j", "g"],
            ["o", "a"], ["o", "b"], ["o", "d"], ["p", "e"], ["r", "c"], 
            ["r", "e"], ["r", "m"], ["r", "n"], ["r", "p"], ["s", "c"],
            ["s", "e"], ["t", "j"], ["t", "l"], ["u", "e"], ["u", "h"], 
            ["u", "o"], ["u", "r"], ["v", "c"], ["v", "o"], ["x", "v"],
            ["y", "q"], ["z", "e"], ["z", "w"]]
pairs_100 = [["d", "b"], ["e", "a"], ["g", "d"], ["h", "b"], ["j", "i"],
            ["k", "h"], ["l", "i"], ["n", "c"], ["n", "h"], ["n", "m"],
            ["o", "c"], ["o", "e"], ["p", "b"], ["p", "d"], ["p", "g"], 
            ["p", "o"], ["q", "b"], ["q", "d"], ["q", "g"], ["q", "p"],
            ["r", "h"], ["t", "f"], ["u", "c"], ["u", "n"], ["v", "u"],
            ["w", "m"], ["w", "u"], ["w", "v"], ["x", "k"], ["y", "g"], 
            ["y", "u"], ["y", "v"], ["z", "s"]]

# In[36]:


import string
import random


## Creating random generator for beginning replacement (first + second placement)
def id_generator_beginning(size = 5, pairs = pairs_10, chars = string.ascii_lowercase):
    result = []
    for pair in pairs:
        placement = random.randint(0, 1)
        if placement == 0:
            pre_generator = ''.join(random.choice(chars) for _ in range(size - 1))
            pair_list = []
            for letter in pair:
                pair_list.append(letter + pre_generator)
        if placement == 1:
            pre_generator = ''.join(random.choice(chars) for _ in range(size - 2))
            prefix = random.choice(chars)
            pair_list = []
            for letter in pair:
                pair_list.append(prefix + letter + pre_generator)    
        result.append(pair_list)
    return result

## Note ##
# size = length of words
# pairs = choose list of pairs to be replaced
# num_pairs = number of pairs chosen from list to be replaced
df = id_generator_beginning(size = 9, pairs = pairs_100)

## Creating random generator for end replacement
def id_generator_end(size = 5, pairs = pairs_10, chars = string.ascii_lowercase):
    result = []
    for pair in pairs:
        placement = random.randint(0, 1)
        if placement  == 0:
            pre_generator = ''.join(random.choice(chars) for _ in range(size - 1))
            pair_list = []
            for letter in pair:
                pair_list.append(pre_generator + letter)
            result.append(pair_list)
        if placement == 1:
            pre_generator = ''.join(random.choice(chars) for _ in range(size - 2))
            pair_list = []    
            postfix = random.choice(chars)
            for letter in pair:
                pair_list.append(pre_generator + letter + postfix)
            result.append(pair_list)
    return result

df = id_generator_end(size = 9, pairs = pairs_100)

## Creating random generator for middle replacement
def id_generator_middle(size = 5, pairs = pairs_10, chars = string.ascii_lowercase):
    result = []
    for pair in pairs:
        pre_generator = ''.join(random.choice(chars) for _ in range(size - 1))
        pair_list = []
        if size == 5:
            placement = 0  
            for letter in pair:
              output = pre_generator[:(2+placement)] + letter + pre_generator[(2+placement):]
              pair_list.append(output)
        if size == 7:
            placement = random.randint(-1, 1)  
            for letter in pair:
              output = pre_generator[:(3+placement)] + letter + pre_generator[(3+placement):]
              pair_list.append(output)
        if size == 9:
            placement = random.randint(-2, 2)  
            for letter in pair:
              output = pre_generator[:(4+placement)] + letter + pre_generator[(4+placement):]
              pair_list.append(output)
        result.append(pair_list)
    return result

## Note ##
# size = length of words
# pairs = choose list of pairs to be replaced
# num_pairs = number of pairs chosen from list to be replaced
# placement = varying the level of middle; 0 = median
df = id_generator_middle(size = 9, pairs = pairs_100)
  
## Creating the same pair - for control group
def id_generator(size = 5, iteration = 20, chars = string.ascii_lowercase):
    result = []
    for n in range(1, iteration):
        pair = []
        pre_generator = ''.join(random.choice(chars) for _ in range(size))
        pair.append(pre_generator)
        pair.append(pre_generator)
        result.append(pair)
    return result
        
df = id_generator(size = 9, iteration = 200)
