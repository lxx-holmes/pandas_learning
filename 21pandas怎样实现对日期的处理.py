#!/usr/bin/env python
# coding: utf-8

# 21pandas怎样实现对日期的处理
# pandas将各种日期格式，统一映射为pandas本身的日期对象，提供强大支持。
# 几个概念：
# 1.pd.to_datetime:pandas的一个函数，能将字符串、列表、series变成日期形式
# 2.Timestamp:pandas表示日期的对象形式
# 3.DatetimeIndex:pandas表示日期的对象列表形式 （Timestamp的列表）
# 其中：
# DatetimeIndex是Timestamp的列表形式
# 单个日期pd.to_datetime会生成timestamp
# 日期列表pd.to_datetime会生成DatetimeIndex
# 问题：怎样统计每周、每月、每季度的最高温度？

# In[6]:


#1.读取天气数据到dataframe
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
#因为一会热要画图，引入这个包来画图
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')
df


# In[7]:


#2.将日期列转换成pandas的日期
df.set_index(pd.to_datetime(df['ymd']),inplace=True)
'''
修改一个对象时：
inplace=True：不创建新的对象，直接对原始对象进行修改；
inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。
'''


# In[8]:


df


# In[9]:


df.index


# In[11]:


df.index[0]


# In[12]:


#3.方便的对DatetimeIndex进行查询
#筛选固定的某一天,返回这一天所有的信息
df.loc['2018-01-05']


# In[13]:


#日期区间
df.loc['2018-01-05':'2018-01-10']


# In[15]:


#按月份前缀筛选
df.loc['2018-03']


# In[16]:


df.loc['2018-07':'2018-09']


# In[17]:


#按年份前缀筛选
df.loc['2018']


# In[ ]:


#4.方便的获取周、月、季度
#https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components


# In[21]:


df.index.isocalendar().week #视频上是df.index.week，但是提示建议使用新方法。


# In[22]:


df.index.month


# In[23]:


df.index.quarter


# In[26]:


#5.统计每周、每月、每个季度的最高温度
#统计每周的温度
df.groupby(df.index.isocalendar().week)['bWendu'].max()
df.groupby(df.index.isocalendar().week)['bWendu'].max().plot()


# In[27]:


df.groupby(df.index.month)['bWendu'].max().plot()


# In[28]:


df.groupby(df.index.quarter)['bWendu'].max().plot()

