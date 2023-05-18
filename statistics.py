#!/usr/bin/env python
# coding: utf-8

# In[15]:


i=[12,65,54,48,12]

count=0
for a in i:
    
    count=count+1
mean=sum/count


# In[16]:


mean


# In[17]:


import numpy as np


# In[18]:


mean=np.mean(i)


# In[19]:


mean


# In[20]:


median=np.median(i)
print(median)


# In[34]:


i=[50,67,24,34,78,43]
median=np.median(i)
print(median)


# In[32]:


i=[50,67,24,34,78,43]
i.sort()
if len(i)==1:
    a=i[len(i)//2]
    b=i[(len(i)//c)+1]
    median=a+b//2
else :
    median=i[(len(i)//2)]
    
print(median)



# In[35]:


i=[50,67,24,34,78,43]
i.sort()
print(i)


# In[39]:


from scipy import stats
i=[50,51,83,50,51]
mode=stats.mode(i)
print(mode)


# In[40]:


import statistics
arr=[1,2,3,4,5]
print(statistics.variance(arr))


# In[41]:


import statistics
arr=[1,2,3,4,5]
print(statistics.stdev(arr))


# In[42]:


import pandas as pd


# In[54]:


train=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\new data set\train.csv")


# In[55]:


train


# In[59]:


print(train["Gender"].isna().sum())
print(train["Married"].isna().sum())
print(train["Dependents"].isna().sum())
print(train["Self_Employed"].isna().sum())
print(train["LoanAmount"].isna().sum())
print(train["Loan_Amount_Term"].isna().sum())
print(train["Credit_History"].isna().sum())


# In[61]:


train.isna().any()


# In[62]:


train[train.columns[train.isna().any()]]


# In[63]:


train["Gender"].value_counts()


# In[64]:


train["Married"].value_counts()


# In[65]:


train["Dependents"].value_counts()


# In[ ]:




train["Dependents"]=train["Dependents"].replace(to_replace="3+",value=4)
# In[69]:


train


# In[70]:


train["Gender"]=(train["Gender"].fillna(train["Gender"].mode()[0]))
train["Married"]=(train["Married"].fillna(train["Married"].mode()[0]))
train["Dependents"]=(train["Dependents"].fillna(train["Dependents"].mode()[0]))
train["Self_Employed"]=(train["Self_Employed"].fillna(train["Self_Employed"].mode()[0]))
train["LoanAmount"]=(train["LoanAmount"].fillna(train["LoanAmount"].mode()[0]))
train["Loan_Amount_Term"]=(train["Loan_Amount_Term"].fillna(train["Loan_Amount_Term"].mode()[0]))
train["Credit_History"]=(train["Credit_History"].fillna(train["Credit_History"].mode()[0]))


# In[71]:


train


# In[72]:


train.head(30)


# In[73]:


train.isna().any()


# In[77]:


train["LoanAmount"]=(train["LoanAmount"].fillna(train["LoanAmount"].mode()[0]))


# In[78]:


train


# In[80]:


train["Self_Employed"]=(train["Self_Employed"].fillna(train["Self_Employed"].mode()[0]))
train.head(30)


# In[87]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
train["LoanAmount"].plot(kind="hist")
plt.show()


# In[85]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[88]:


train["LoanAmount"].plot(kind="hist",color="pink")
plt.show()


# In[89]:


train["LoanAmount"].plot(kind="hist",color="pink",alpha=0.4)
plt.show()


# In[96]:


train["LoanAmount"].plot(kind="hist",color="pink",alpha=0.6,bins=20)
plt.show()


# In[102]:


train["LoanAmount"].plot(kind="hist",color="pink",alpha=1)
plt.xlabel("LoanAmount")
plt.ylabel("count")
plt.title("Histogram")
plt.show()


# In[104]:


count=train["LoanAmount"].value_counts()


# In[106]:


count.head(40)

