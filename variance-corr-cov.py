#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")
df


# In[6]:


sns.distplot(df["Sepal.Width"])
plt.show()


# In[8]:


sns.regplot(x="Sepal.Length",y="Sepal.Width",data=df)
plt.show()


# In[10]:


g=sns.FacetGrid(df,col="Species")
g.map(plt.hist,"Sepal.Length")
plt.show()


# In[11]:


g=sns.FacetGrid(df,col="Species")
g.map(plt.scatter,"Sepal.Length","Sepal.Width")
plt.show()


# In[12]:


g=sns.FacetGrid(df,col="Species")
g.map(plt.scatter,"Petal.Length","Petal.Width")
plt.show()


# In[13]:


g=sns.FacetGrid(df,row="Species")
g.map(plt.hist,"Sepal.Length")
plt.show()


# In[15]:


g=sns.FacetGrid(df,row="Species")
g.map(plt.scatter,"Petal.Length","Petal.Width")
plt.show()


# In[16]:


sns.jointplot(x="Sepal.Length",y="Sepal.Width",data=df)
plt.show()
sns.jointplot(x="Sepal.Length",y="Sepal.Width",data=df,kind="reg")
plt.show()


# In[19]:


sns.pairplot(df)
plt.show()


# In[20]:


sns.pairplot(df,hue="Species")
plt.show()


# In[21]:


df=pd.DataFrame({
    "a":[1,3,4,6,8],
    "b":[2,3,5,6,8],
    "c":[6,5,4,3,2],
    "d":[5,4,3,4,6],
})
df


# In[22]:


(np.square(df["a"]-df["a"].mean())).sum()/(df.shape[0]-1)


# In[24]:


sns.boxplot(data=df.melt(),
           x="variable",
           y="value")


# In[25]:


np.var(df[["a","b","c","d"]],ddof=1)


# In[26]:


np.var(df[["a","b","c","d"]],ddof=0)#not perfect because take a,b,c,d value


# In[27]:


np.var(df[["a"]],ddof=1)


# In[28]:


#positive covarience
plt.scatter(df["a"],df["b"])
plt.xlabel("a")
plt.ylabel("b")


# In[30]:


#negative covarience
plt.scatter(df["b"],df["c"])
plt.xlabel("b")
plt.ylabel("c")


# In[31]:


#positive covarience
plt.scatter(df["c"],df["d"])
plt.xlabel("c")
plt.ylabel("d")


# In[33]:


((df["a"]-df["b"].mean())*(df["b"]-df["b"].mean())).sum()/(df.shape[0]-1)


# In[34]:


np.cov(df["a"],df["b"])


# In[35]:


np.cov(df["b"],df["c"])


# In[36]:


np.cov(df["c"],df["d"])


# In[38]:


def covaience(x,y):
    mean_x=sum(x)/float(len(x))
    mean_y=sum(y)/float(len(y))
    
    sub_x=[i-mean_x for i in x]
    sub_y=[i-mean_y for i in y]
    num=sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
    dom=len(x)-1
    
    cov=num/dom
    return cov

x=df["a"]
y=df["b"]

covaience(x,y)


# In[ ]:




