
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from collections import OrderedDict


# In[2]:

df = pd.read_table(r'/Users/xiechangrun/Desktop/classu.txt')


# In[43]:

fil = open(r'/Users/xiechangrun/Desktop/class8.txt', 'r')
word = []
data = []
n=0
for line in fil:
    words = line.split()
    word.extend(words)


# In[44]:

lens = len(word)
print(lens)


# In[45]:

while lens - n > 5:
    info = OrderedDict()
    info['school_name'] = word[n]
    info['dept'] = word[n+1]
    info['code'] = word[n+2]
    info['num_want'] = word[n+3]
    info['num_act'] = word[n+4]
    data.append(info)
    n += 5


# In[47]:

df = DataFrame(data)
df.to_csv(r'/Users/xiechangrun/Desktop/try0.csv',encoding='utf-8')


# In[49]:

df2= pd.read_csv(r'/Users/xiechangrun/Desktop/try0.csv',encoding='utf-8')


# In[50]:

df2.head()


# In[ ]:



