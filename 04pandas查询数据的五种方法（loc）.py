#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.set_index("ymd",inplace=True)


# In[15]:


df.index
df.head()


# In[16]:


df.loc[:,"bWendu"]=df["bWendu"].str.replace("℃","").astype("int32") #select all rows for column bWendu, and delete ℃
df.loc[:,"yWendu"]=df["yWendu"].str.replace("℃","").astype("int32") #select all rows for column yWendu, and delete ℃
df.head()


# In[17]:


df.loc['2018-01-03','bWendu']#输入横纵坐标，查到一个值


# In[18]:


df.loc['2018-01-03',['bWendu','yWendu']] #锁定一行，但是多列，得出series数据


# In[19]:


df.loc[['2018-01-03','2018-01-03'],'bWendu'] #得到某几天的最低温度


# In[20]:


df.loc[['2018-01-03','2018-01-03'],['bWendu','yWendu']] #得到某几天的最低温度和最高温度


# In[23]:


df.loc['2018-01-03':'2018-01-05','bWendu']


# In[24]:


df.loc['2018-01-03','bWendu':'fengxiang']


# In[26]:


df.loc['2018-01-01':'2018-01-05','bWendu':'fengxiang']


# In[27]:


df.loc[df['yWendu']<-10,:] #找出当年所有最低温度小于-10的日子，显示所有信息


# In[30]:


df.loc[(df['bWendu']<=30)&(df['yWendu']>=15)&(df['tianqi']=='晴')&(df['aqiLevel']==1)] #找北京的“好天气”


# In[29]:


(df['bWendu']<=30)&(df['yWendu']>=15)&(df['tianqi']=='晴')&(df['aqiLevel']==1) #括号里是布尔值series


# In[31]:


#用lambda表达式，进行条件查询
df.loc[lambda df: (df['bWendu']<=30)&(df['yWendu']>=15),:]


# In[33]:


#编一个函数，查询9月份空气质量为优的日子
def query_my_data(df):
    return df.index.str.startswith('2018-09')&df['aqiLevel']==1
query_my_data(df) #用这个function，得到一个布尔值的series，其中符合条件的行为true


# In[34]:


df.loc[query_my_data, :] #根据上面的布尔值series，把true的行显示出来

