#!/usr/bin/env python
# coding: utf-8

# # Pandas怎么处理日期索引的缺失？
# 问题：按日期统计的数据，缺失了某天，导致数据不全该怎么补充日期？
# 可以用两种方法实现：
# 1.DataFrame.reindex，调整dataframe的索引以适应新的索引
# 2.DataFrame.resample,可以对时间序列重采样，支持补充缺失值

# In[1]:


#问题：如果缺失了索引该怎么填充？
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.DataFrame({
    'pdate':['2019-12-01','2019-12-02','2019-12-04','2019-12-05'],
    'pv':[100,200,400,500],
    'uv':[10,20,40,50]
})
df


# In[3]:


df.set_index('pdate').plot()


# 这里缺失了12月3号的数据，怎么能补回来呢？

# In[4]:


#方法1：使用pandas.reindex方法
#1.将df的索引变成日期索引
df_date=df.set_index('pdate')
df_date


# In[5]:


df_date.index


# In[6]:


#将df的索引设置为日期索引
df_date=df_date.set_index(pd.to_datetime(df_date.index))
df_date


# In[7]:


df_date.index


# In[8]:


#2.使用pandas.reindex填充缺失的索引
#生成完整的日期序列
pdates=pd.date_range(start='2019-12-01',end='2019-12-05')
pdates


# In[9]:


df_date_new=df_date.reindex(pdates, fill_value=0)
df_date_new


# In[10]:


df_date_new.plot()


# In[ ]:


#方法2：使用pandas.resample方法
#1.先将索引变成日期索引


# In[11]:


df


# In[15]:


#df_new2=df.set_index('pdate')
df_new2=df.set_index(pd.to_datetime(df['pdate'])).drop('pdate',axis=1)
df_new2


# In[16]:


df_new2.index


# In[ ]:


#2.使用dateframe的resample的方法按天重采样


# resample的含义：
# 改变数据的事件频率，比如把天数据变成月份，或者把小时数据变成分钟级别
# 
# resample的语法：
# (DataFrame or Series).resample(arguments).(aggregate function) #聚合函数
# 
# resample的采样规则参数：（日，周，年等简写符号）
# pandas网站找offset aliases
# 
# 

# In[17]:


#由于采样会让区间变成一个值，所以需要指定mean等采样值的设定方法
df_new2=df_new2.resample('D').mean().fillna(0)
df_new2


# In[18]:


df_new2.resample('2D').mean() #对以上df，每两天进行采样，看到五行数据变成了三行。
#一号二号变成了一行，取了两个数据的平均值；三号四号同样；五号只有一天，还是它自己。

