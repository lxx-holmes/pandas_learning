#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df=pd.read_csv("C:/Users/Susie X Li/Desktop/pandas学习/beijing_tianqi_2018.csv")
df.head()


# In[14]:


#第一种方法：直接赋值的方法，把温度列改成不带°C
df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')
df.head()


# In[15]:


#新增一列温差
df.loc[:,"wencha"]=df['bWendu']-df['yWendu']
df.head()


# In[16]:


#第二种方法：df.apply
#例题：添加一列“温度类型”，大于33度是高温，低于-10是低温，否则是常温
def get_wendu_type(x): #传入一个series X （一行数据），进行判断
    if x['bWendu']>33:
        return '高温'
    if x['yWendu']<-10:
        return '低温'
    return '常温'

df.loc[:,"wendu_type"]=df.apply(get_wendu_type, axis=1) #axis=1表示新加一个column。对df数据集的每一行进行判断，返回温度类型，放在新列
df["wendu_type"].value_counts()


# In[19]:


#第三种方法：df.assign
#可以同时添加多个新的列
df=df.assign(
    yWendu_huashi=lambda x: x['yWendu']*9/5+32,
    bWendu_huashi=lambda x: x['bWendu']*9/5+32
)
#lambda x表示这个函数，函数的内容是对yWendu和bWendu进行操作
'''匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
https://www.cnblogs.com/kaishirenshi/p/8611358.html'''


# In[20]:


pd.set_option('display.max_columns', None)
df.head() #为什么显示不出新增的两列？？？ok了，要写df=df.assign...
print(df)


# In[21]:


#第四种方法：按条件选择分组，分别赋值
#先创建空列
df['wencha_type']=''
df.loc[df['bWendu']-df['yWendu']>10,'wencha_type']='温差大'
df.loc[df['bWendu']-df['yWendu']<=10,'wencha_type']='温差正常'
df['wencha_type'].value_counts()

