#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#07pandas对缺失值的处理
'''
isnull,notnull：检查是否空值，可用于df和series

dropna: 
axis：删除行还是列,{0 or 'index'按行，1 or 'columns'按列} default 0
how：如果等于any则任何值为空都删除，如果等于all则所有值都为空才删除
inplace：true则修改当前df，否则返回新df

fillna:填充空值
value:用于填充的值，可以是单个值，或者字典（key是列名，value是值）
method：等于ffill使用前一个不为空的值填充foward fill;等于bfill使用后一个不为空的值填充backword fill
axis：按行还是列填充，{0 or 'index',1 or 'columns'}
inplace: true则修改当前df，否则返回新df


# In[1]:


import pandas as pd
studf=pd.read_excel("C:/Users/Susie X Li/Desktop/pandas学习/student_excel.xlsx",skiprows=2)
studf


# In[2]:


studf.isnull()


# In[3]:


studf['分数'].isnull()


# In[4]:


studf['分数'].notnull() #跟isnull结果正好相反


# In[5]:


studf.loc[studf['分数'].notnull(),:]


# In[6]:


#删掉全是空值的列
studf.dropna(axis='columns',how='all',inplace=True)
studf


# In[7]:


#删除掉全是空值的行
studf.dropna(axis='index',how='all',inplace=True)
studf


# In[13]:


#将分数列为空的填充为0分
studf.loc[:,'分数']=studf.fillna({'分数':0})
#等同于: studf.loc[:,'分数'].fillna(0) 意思是所有行，选出分数这一列；对这一列进行fillna(0)操作。
studf


# In[14]:


#将姓名的缺失值填充
studf.loc[:,'姓名']=studf.loc[:,'姓名'].fillna(method='ffill')
studf


# In[15]:


#save clean excel file
studf.to_excel("C:/Users/Susie X Li/Desktop/pandas学习/student_excel_susiecleaned.xlsx",index=False) #false表示第一列不是0-10的index

