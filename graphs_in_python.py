#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd


# In[5]:


i=[3,5,7,12,13,14,21,23,23,23,23,29,40,56]
print(np.mean(i))


# In[6]:


i=[3,5,7,12,13,14,21,23,23,23,23,29,40,56]
print(np.median(i))


# In[7]:


i=[3,5,7,12,13,14,21,23,23,23,23,29,40,56]
print(stats.mode(i))


# In[13]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")


# In[21]:


df.head(30)


# In[17]:


count=df["Species"].value_counts()
count


# In[18]:


count.plot(kind="bar")


# In[19]:


count.plot(kind="bar",color=["red","green","blue"])


# In[20]:


count.plot(kind="bar",color=["red","green","blue"])
plt.xlabel("Speices")
plt.ylabel("count")
plt.title("bar chart")
plt.show()


# In[61]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\orders.csv")
df


# In[41]:


count=df["Payment Terms"].value_counts()
count


# In[42]:


count.plot(kind="bar")


# In[39]:


count.plot(kind="bar")
plt.xlabel("payment term")
plt.ylabel("count")
plt.title("bar chart")
plt.show()


# In[35]:


count=df["Place of Shipment"].value_counts
count


# In[34]:


count=df["Place of Shipment"].value_counts()
count.plot(kind="bar")
plt.xlabel("Place of Shipment")
plt.ylabel("count")
plt.title("bar chart")
plt.show()


# In[37]:


count=df["Place of Shipment"].value_counts()
count.plot(kind="bar")
plt.xlabel("Place of Shipment")
plt.ylabel("count")
plt.title("bar chart")
plt.xticks(rotation=90)
plt.show()


# In[44]:


count.plot(kind="pie")
plt.xlabel("payment term")

plt.show()


# In[45]:


count.plot(kind="pie",autopct="%.2f%%")
plt.xlabel("payment term")

plt.show()


# In[46]:


#curner density graph
count.plot(kind="kde")


# In[68]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")
df["Sepal.Length"].plot(kind="kde")


# In[59]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")
df.plot(kind="scatter",x="Sepal.Length",y="Sepal.Width")
plt.xlabel("Sepal.Length")
plt.ylabel("Sepal.Width")
plt.title("Scatter plot")
plt.show()


# In[65]:


import seaborn as sns
sns.countplot(x="Payment Terms",data=df)
plt.show()


# In[70]:


import seaborn as sns
sns.boxplot(x="Species",y="Sepal.Length",data=df)
plt.show()


# In[71]:


import seaborn as sns
sns.boxplot(y="Sepal.Length",data=df)
plt.show()


# In[73]:


import seaborn as sns
sns.boxplot(x="Sepal.Length",data=df)
plt.show()


# In[79]:


df


# In[77]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")


# In[78]:


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")
sns.scatterplot(x="Sepal.Length",y="Sepal.Width",hue="Species",data=df)
plt.show()


# In[ ]:




