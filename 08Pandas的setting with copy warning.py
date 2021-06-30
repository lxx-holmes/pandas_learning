#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''08pandas的SettingWithCopyWarning警报复现、原因、解决方案
'''
import pandas as pd
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.head(3)


# In[2]:


df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')
df.head(3)


# In[3]:


#只选出3月的数据用于分析
condition=df['ymd'].str.startswith('2018-03')
#设置温差
df[condition]['wencha']=df['bWendu']-df['yWendu']


# In[4]:


df[condition].head()
#有时候成功，有时候不成功。原因如下：
'''
发出警告的代码df[condition]['wencha']=df['bWendu']-df['yWendu']
相当于：df.get(condition).set(wen_cha)，第一步骤get发出了警报
先get后set，get得到的dataframe可能是view也可能是copy, pandas发出警告
view：df的一个子视图；copy：它是一个新的df，跟原来的df没有关系了。
核心要诀：pandas的dataframe修改写操作，只允许在源dataframe上进行，一步到位。两个解决方法如下：
'''


# In[5]:


#3.解决方法1，将get+set的两步操作，变成set的一步操作
df.loc[condition,"wen_cha"]=df['bWendu']-df['yWendu']
df[condition].head()


# In[6]:


#解决方法2：使用copy复制dataframe，得到新的dataframe，在这个df上操作
df_month3=df[condition].copy()#得到一个新的dataframe，叫做df_month3
df_month3.head()


# In[7]:


df_month3['wen_cha_2']=df['bWendu']-df['yWendu']
df_month3.head()


# In[ ]:


'''
总之，pandas不允许先筛选dataframe，再进行修改写入
要么使用loc实现一个步骤直接修改源dataframe
要么先复制一个新的dataframe，再一个步骤执行修改
'''

