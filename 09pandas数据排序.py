#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#9.pandas数据排序
'''
series的排序：
Series.sort_values(ascending=True, inplace=False) 
ascending=true是升序，false则是降序；inplace：是否修改原始series

dataframe的排序：
DataFrame.sort_values(by, ascending=True, inplace=False)
by: 字符串或者list<字符串>，单列排序或者多列排序
ascending: bool或者List，升序还是降序，如果list对应的by的多列
inplace:是否修改原有dataframe
'''


# In[1]:


import pandas as pd
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')
df.head(3)


# In[2]:


df['aqi'].sort_values()


# In[3]:


df['aqi'].sort_values(ascending=False)


# In[4]:


df['tianqi'].sort_values()


# In[5]:


#dataframe排序
#单列排序
df.sort_values(by='aqi')


# In[6]:


df.sort_values(by='aqi',ascending=False)


# In[7]:


#2.2多列排序
df.sort_values(by=['aqiLevel','bWendu']) #先排列空气质量，然后按最高温度排序


# In[8]:


df.sort_values(by=['aqiLevel','bWendu'],ascending=False)


# In[9]:


df.sort_values(by=['aqiLevel','bWendu'],ascending=[True, False]) #多列分别指定升序和降序

