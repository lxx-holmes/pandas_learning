#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#10pandas字符串处理
'''
1.使用方法：先获取series的str属性，然后在属性上调用函数
2.只能在字符串列上使用，不能数字列上使用
3.dataframe上没有str属性和处理方法
4.series.str并不是python原生字符串，而是pandas自己的一套方法，不过大部分和原生str很相似

网页：pandas.pydata.org里的string handling
'''


# In[1]:


import pandas as pd
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.head()
df.dtypes #object列可以直接使用字符串方法。


# In[2]:


#1.获取series的str属性，使用各种字符串处理函数
df['bWendu'].str


# In[3]:


df['bWendu'].str.replace('℃','')


# In[4]:


df['bWendu'].str.isnumeric() #字符串是不是数字？返回全是false，说明不是。


# In[ ]:


df['aqi'].str.len() #会报错，因为str属性不能用在数字上


# In[5]:


#2.使用str的startswith, contains等得到bool的series可以做条件查询
condition=df['ymd'].str.startswith('2018-03')


# In[6]:


condition


# In[7]:


df[condition].head()
#把df按condition里的条件，切出一块来


# In[ ]:


#3.需要多次str处理的链式操作
'''
怎样提取201803这样的数字月份？
1.先将日期2018-03-31替换成20180331的格式
2.提取月份字符串201803'''


# In[8]:


df['ymd'].str.replace('-','')


# In[ ]:


df['ymd'].str.replace('-','').slice(0,6) #这个会报错，因为slice不能直接用在series上，要用在字符串上
#怎么改？先用str.replace，再用str.slice，即可。因为str是series上的属性。


# In[9]:


df['ymd'].str.replace('-','').str.slice(0,6)


# In[10]:


df['ymd'].str.replace('-','').str[0:6]


# In[11]:


#4.使用正则表达式的处理
#添加新列
def get_nianyueri(x):
    year, month, day=x['ymd'].split('-')
    return f'{year}年{month}月{day}日'
df['中文日期']=df.apply(get_nianyueri, axis=1)


# In[12]:


df['中文日期']


# In[13]:


#怎样将年月日三个中文字去掉？
df['中文日期'].str.replace('年','').str.replace('月','').str.replace('日','')


# In[14]:


#series.str默认就开启了正则表达式模式
#方法2：正则表达式替换
df['中文日期'].str.replace('[年月日]','') #只要遇到年月日的任何一个，都替换成空

