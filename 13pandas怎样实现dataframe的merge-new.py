#!/usr/bin/env python
# coding: utf-8

# In[1]:


#13pandas怎样实现dataframe的merge
#1。电影数据集的join实例
import pandas as pd
df_ratings=pd.read_csv(
    "C:/Users/Susie X Li/Desktop/pandas学习/movies/ratings.dat",
    sep="::",
    engine='python',#系统会默认双冒号是正则表达式，所以指定engine=python，表示它就是正常的双冒号。
    names='UserID::MovieID::Rating::Timestamp'.split("::")
)
df_ratings.head()


# In[2]:


df_users=pd.read_csv(
    "C:/Users/Susie X Li/Desktop/pandas学习/movies/users.dat",
    sep="::",
    engine='python',#系统会默认双冒号是正则表达式，所以指定engine=python，表示它就是正常的双冒号。
    names='UserID::Gender::Age::Occupation::Zip-code'.split("::")
)
df_users.head()


# In[3]:


df_movies=pd.read_csv(
    "C:/Users/Susie X Li/Desktop/pandas学习/movies/movies.dat",
    sep="::",
    engine='python',#系统会默认双冒号是正则表达式，所以指定engine=python，表示它就是正常的双冒号。
    names='MovieID::Title::Genres'.split("::")
)
df_movies.head()


# In[4]:


df_ratings_users=pd.merge(
    df_ratings, df_users, left_on="UserID",right_on="UserID", how="inner"
)
#inner:两边都有这个userID才会被保留，否则丢弃。
df_ratings_users.head()


# In[5]:


df_ratings_users_movies=pd.merge(
    df_ratings_users, df_movies, left_on="MovieID", right_on="MovieID", how="inner"
)
df_ratings_users_movies.head(20)


# In[ ]:


#2.理解merge时数量的对齐关系
'''one-to-one: 一对一，比如（学号，姓名）merge（学号，年龄），结果条数为1*1，一个学号只有一个姓名，一个年龄
one-to-many:一对多关系，左边唯一key，右边不唯一key
比如（学号，姓名）merge（学号，【语文成绩，数学成绩，英语成绩】），一个学号只有一个姓名，多个成绩
结果条数为1*N
many-to-many:多对多关系，左边右边都是不唯一的
比如（学号，【语文成绩，数学成绩，英语成绩】）merge（学号，【篮球，足球，乒乓球】）
结果条数为M*N
'''
#2.1 one-to-one 一对一关系的merge


# In[6]:


left=pd.DataFrame({'sno':[11,12,13,14],
                  'name':['a','b','c','d']
                  })
right=pd.DataFrame({'sno':[11,12,13,14],
                  'age':['21','22','23','24']
                  })
pd.merge(left,right,on='sno')


# In[7]:


#2.2 one to many 一对多关系的merge
#注意：数据会被复制
left=pd.DataFrame({'sno':[11,12,13,14],
                  'name':['a','b','c','d']
                                     })
right=pd.DataFrame({'sno':[11,11,11,12,12,13],
                  'grade':['语文88','数学90','英语75','语文66','数学90','英语20']
                                     })
pd.merge(left,right,on='sno') #数目以多的一边为准


# In[9]:


#2.3 many-to-many 多对多关系的merge
#注意：结果数量会出现乘法
left=pd.DataFrame({'sno':[11,11,12,12,12],
                  '爱好':['篮球','羽毛球','乒乓球','篮球','足球']
                                     })
right=pd.DataFrame({'sno':[11,11,11,12,12,13],
                  'grade':['语文88','数学90','英语75','语文66','数学90','英语20']
                                     })
pd.merge(left,right,on='sno')
#比如学号11出现了6条数据


# left join:完全保留左边的数据，right join：完全保留右边的数据
# inner join:
# full outer join:

# In[11]:


left=pd.DataFrame({
    'key':['KO','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right=pd.DataFrame({
    'key':['KO','K1','K4','K5'],
    'C':['C0','C1','C4','C5'],
    'D':['D0','D1','D4','D5']
})
left


# In[12]:


right


# In[13]:


#3.1 inner join, 默认
#左右两边都有的key，才会出现在结果里。只剩下了K0,K1
pd.merge(left,right,how='inner')


# In[14]:


#3.2 left join
#左边的都会出现在结果里，右边的如果无法匹配则为null
pd.merge(left,right,how='left')


# In[15]:


#3.3 right join
pd.merge(left,right,how='right')


# In[17]:


#3.4 outer join
#左边，右边都会出现在结果里，左边的如果无法匹配则为null
pd.merge(left,right,how='outer')


# In[18]:


#4.如果出现非key的字段重名怎么办
left=pd.DataFrame({
    'key':['KO','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right=pd.DataFrame({
    'key':['KO','K1','K4','K5'],
    'A':['A10','A11','A14','A15'],
    'D':['D0','D1','D4','D5']
})


# In[19]:


left


# In[20]:


right


# In[21]:


pd.merge(left,right,on='key')
#两个A变成了A_x和A_y进行区分


# In[22]:


pd.merge(left,right,on='key',suffixes=('_left','_right'))

