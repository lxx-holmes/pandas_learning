#!/usr/bin/env python
# coding: utf-8

# 11.pandas的axis参数怎么理解？
# axis=0或者Index：
# -如果是单行操作，就是指某一行
# -如果是聚合操作，指的是跨行cross rows
# axis=1或columns:
# -如果是单列操作，就是指某一列
# -如果是聚合操作，指的是跨列cross columns
# 
# 按照哪个axis，就是这个axis要动起来（类似被for遍历），其他的axis保持不动

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


#构造一个3*4的df
df=pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A','B','C','D']
)
df


# In[4]:


#1.单列drop，就是删除某一列
df.drop("A",axis=1)


# In[5]:


#2.单行drop，就是删除某一行
df.drop(1,axis=0)


# In[6]:


#3.按axis=0/index执行mean聚合操作
#反直觉：输出的不是每行的结果，而是每列的结果
df


# In[7]:


df.mean(axis=0) #反直观：得出四列的mean数据，而不是三行的数据。四列不动，每列内部按行遍历。


# In[8]:


#4.按axis=1/columns执行mean聚合操作
df


# In[9]:


df.mean(axis=1)


# In[10]:


#5.再次举例，加深理解
def get_sum_value(x):
    return x['A']+x['B']+x['C']+x['D']
df['sum_value']=df.apply(get_sum_value, axis=1)


# In[11]:


df

