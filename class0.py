
# coding: utf-8

# In[186]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from collections import OrderedDict

df = pd.read_table(r'/Users/xiechangrun/Desktop/nameu.txt')


# In[93]:

data = pd.read_csv(r'/Users/xiechangrun/Desktop/name_sep.csv',encoding='utf-8')


# In[94]:

data.head()


# In[3]:

df.to_csv('try1.csv')


# In[34]:

fi = open(r'/Users/xiechangrun/Desktop/nameu.txt', 'r')
word = []
index = []
name = []
index_range = []
index_more = []
for line in fi:
    words = line.split()
    word.append(words)
    
    


# In[35]:

count = 0
for words in word:
    for each in words:
        if each.isdigit() == 1:
            index_range.append(count)
            count = 0
            index.append(each)
        else:
            count += 1
            name.append(each)
            
del index_range[0]
del name[0]


# In[36]:

for i in range(len(index_range)):
    lens = np.repeat(index[i],index_range[i])
    index_more.extend(lens)


# In[47]:

print(len(index_more))
print(len(name))


# In[57]:

combined = dict(enumerate(zip(index_more,name)))


# In[134]:

df.to_csv('name2_sep.csv',encoding='utf-8')


# In[103]:

df2 = DataFrame(combined)


# In[104]:

df2.head()


# In[108]:

df = DataFrame({'key':combined.keys(),'name':combined.values()})


# In[132]:

df['tag'] = df['name'].astype(str).str.split(',').str[0]
df['tag'] = df['tag'].str.split('(').str[1] #.str.replace('\'','')
df['number'] = df['name'].astype(str).str.split(',').str[1].str[0:10]
df['number'] = df['number'].str.replace('\'','')


# In[129]:

df['names'] = df['name'].astype(str).str.split(',').str[1].str[10:]
df['names'] = df['names'].str.replace('\'','')
df['names'] = df['names'].str.replace(')','')


# In[133]:

df.head()


# In[264]:

data = pd.read_csv(r'/Users/xiechangrun/Desktop/name_all.csv')
data_class = pd.read_csv(r'/Users/xiechangrun/Desktop/classu10.csv')


# In[262]:

data_class.head()


# In[238]:




# In[211]:




# In[240]:




# In[241]:




# In[224]:




# In[242]:




# In[225]:




# In[266]:

data2 = data[['tag','number','first','last','bebe']]
data2 = data2.rename(columns={'tag':'dcode'})


# In[268]:

data2.to_csv('name_0426.csv',encoding='utf-8')


# In[253]:

#data2['dcode'] = data2['dcode'].str.replace('\'','')
data2.head()


# In[267]:

data2['num_of_student'] = data2['number'].count() 


# In[254]:

data_school = data2.drop_duplicates(subset='dcode')
data_school['dcode'].count()


# In[255]:

data2['num_of_school'] = data2.groupby('dcode')['number'].transform('count')


# In[258]:

most_school = data2.sort('num_of_school',ascending=False)


# In[259]:

most_school_10 = most_school.drop_duplicates(subset='dcode')


# In[257]:

most_school_10[0:10]


# In[247]:

most_school_10.rename(columns={'tag':'dcode'})


# In[ ]:



