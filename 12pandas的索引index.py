#!/usr/bin/env python
# coding: utf-8

# 12.pandas的索引index
# 把数据储存于普通的column列也能用于数据查询，那使用index有什么好处？
# index的用途总结：
# 1.更方便的数据查询
# 2.使用index可以获得性能提升
# 3.自动的数据对齐功能 （pandas隐含强大特性）
# 4.更多更强大的数据结构支持

# In[1]:


import pandas as pd
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/ml-latest-small/ratings.csv")
df.head()


# In[2]:


df.count()


# In[3]:


#1.使用index查询数据
#drop=False，让索引还保持在column，要不然变成索引的那一列就被删掉了。
df.set_index('userId',inplace=True, drop=False) 
df.head()


# In[4]:


df.index


# In[6]:


#使用column的condition查询方法
df.loc[df['userId']==500].head() #此时是使用userId这一列进行查询的，而不是index


# In[7]:


df.loc[500].head() #可以看出，使用Index查询可以简化一步。


# In[ ]:


#2.使用index会提升查询性能
'''如果Index是唯一的，pandas会使用哈希表优化，查询性能为O（1）
如果index不是唯一的，但是有序，pandas会使用二分查找算法，查询性能为O(logN)
如果Index是完全随机的，那么每次查询都要扫描全表，查询性能为O（N）
N越来越大时，前两种表现还是很好，但是第三种完全随机数据，查询时间会指数上升。所以要想查得快，索引要有序。


# In[8]:


#实验1：完全随机的顺序查询
#将数据完全打散
from sklearn.utils import shuffle
df_shuffle=shuffle(df)
df_shuffle.head()


# In[9]:


#index是否单调递增？
df_shuffle.index.is_monotonic_increasing #答案是false，因为是随机的，不是单调递增


# In[10]:


#是否是unique的index?是的话pandas将使用哈希查询，速度最快
df_shuffle.index.is_unique #当然也不是


# In[11]:


#计时，查询id=500数据性能
get_ipython().run_line_magic('timeit', 'df_shuffle.loc[500]')


# In[12]:


#实验2：将index排序后的查询
#首先用sort_index对索引进行排序
df_sorted=df_shuffle.sort_index()
df_sorted.head()


# In[13]:


df_sorted.index.is_monotonic_increasing


# In[14]:


df_sorted.index.is_unique


# In[15]:


get_ipython().run_line_magic('timeit', 'df_sorted.loc[500]')


# In[16]:


#3.使用index能自动对齐数据
#包括series和dataframe
s1=pd.Series([1,2,3],index=list('abc'))
s1


# In[17]:


s2=pd.Series([2,3,4],index=list('bcd'))
s2


# In[18]:


s1+s2 #b,c是两个df中对应的数相加，a和d由于找不到对应的，无法相加


# In[ ]:


'''
使用index更多更强大的数据结构支持
categoricalIndex，基于分类数据的Index，提升性能；
MultiIndex，多维索引，用于groupby多维聚合后结果等；
DatetimeIndex，时间类型索引，强大的日期和时间的方法支持；
'''

