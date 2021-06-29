#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''pandas数据统计函数
1.汇总类统计
2.唯一去重和按值计数
3.相关系数和协方差'''
import pandas as pd
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.head(3)


# In[3]:


df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')
df.head(3)


# In[4]:


#1.汇总类统计
#一下子提取所有数字列统计结果
df.describe()


# In[5]:


df['bWendu'].mean()


# In[6]:


df['bWendu'].max()


# In[8]:


df['bWendu'].min()


# In[10]:


#2.唯一去重和按值计数
#2.1唯一性去重
df['fengxiang'].unique()


# In[11]:


df['tianqi'].unique()


# In[12]:


df['fengli'].unique()


# In[13]:


#2.2按值计数
df['fengxiang'].value_counts()


# In[14]:


df['tianqi'].value_counts()


# In[15]:


df['fengli'].value_counts()


# In[16]:


#3.相关系数和协方差
#协方差矩阵
df.cov()
#相关系数=协方差/两个项目标准差之积.


# In[17]:


df.corr()


# In[18]:


df['aqi'].corr(df['bWendu'])


# In[19]:


df['aqi'].corr(df['bWendu']-df['yWendu'])


# In[ ]:


#机器学习特征工程的一个例子

