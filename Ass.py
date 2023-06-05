#!/usr/bin/env python
# coding: utf-8

# # ********ASS ON HYPOTHESIS TEST************

# # Find the relationships between the following variables:Housing.csv

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# In[4]:


housing= pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\Datasets\Housing.csv")
housing


# In[7]:


housing.columns


# # 1. Price and lot size

# In[9]:


#numerical and numerical data 
# by coefficent correlation


# In[11]:


housing['price'].corr(housing['lotsize'])


# In[12]:


sns.scatterplot(data=housing, x='price',y='lotsize')
plt.show()


# In[13]:


#price  doesnot fully related to lotsize


# # 2. Price and Storeys(categorical)

# In[14]:


#numerical and categorical data 
# by ANOVA 


# In[17]:


housing.groupby('stories').mean()


# In[18]:


house = ols('price ~ stories', data=housing).fit()
table = anova_lm(house, typ=2)
print(table)


# In[20]:


#p-value< 0.05
#H0 is rejected with 5% of significances so all prices might not be having 
#same effectfor finding which price is not equal 
# Tukeys method


# In[21]:


compare = pairwise_tukeyhsd(housing['price'], 
                            housing['stories'], alpha=0.05)
pd.DataFrame(compare._results_table.data)


# In[ ]:


#4>3>2>1
#if no of stories is increaes then price is increases
#stories is may be dependent on price


# In[24]:


sns.boxplot(x="stories",y='price', data=housing)
plt.show()


# In[25]:


cts = housing.groupby('stories')['price'].mean()
plt.bar(cts.index, cts)
plt.show()


# # 3. Price and Driveway

# In[26]:


#numerical and categorical data 
# by ANOVA 


# In[30]:


housing.groupby('driveway').mean()


# In[29]:


house = ols('price ~ driveway', data=housing).fit()
table = anova_lm(house, typ=2)
print(table)


# In[31]:


#p-value< 0.05
#H0 is rejected with 5% of significances so all prices might not be having 
#same effectfor finding which price is not equal 
# Tukeys method


# In[32]:


compare = pairwise_tukeyhsd(housing['price'], 
                            housing['driveway'], alpha=0.05)
pd.DataFrame(compare._results_table.data)


# In[ ]:


#yes>no
#if no of driveway is increaes then price is increases
#driveway is may be dependent on price


# In[33]:


sns.boxplot(x="driveway",y='price', data=housing)
plt.show()


# In[34]:


cts = housing.groupby('driveway')['price'].mean()
plt.bar(cts.index, cts)
plt.show()


# # 4. Lot Size and bedrooms(categorical)

# In[35]:


#numerical and categorical data 
# by ANOVA 


# In[36]:


house = ols('lotsize ~ bedrooms', data=housing).fit()
table = anova_lm(house, typ=2)
print(table)


# In[37]:


#p-value< 0.05
#H0 is rejected with 5% of significances so all lotsize might not be having 
#same effect for finding which lotsize is not equal 
# Tukeys method


# In[38]:


compare = pairwise_tukeyhsd(housing['lotsize'], 
                            housing['bedrooms'], alpha=0.05)
pd.DataFrame(compare._results_table.data)


# In[ ]:





# In[40]:


sns.boxplot(x="bedrooms",y='lotsize', data=housing)
plt.show()


# In[43]:


cts = housing.groupby('bedrooms')['lotsize'].mean()
plt.bar(cts.index, cts)
plt.show()


# # 5. Driveway and Recreation room

# In[44]:


#categorical and categorical data 
# by Chi square test 


# In[46]:


pd.crosstab(index=housing['driveway'], 
            columns=housing['recroom'],
            margins=True)


# In[47]:


ctab=pd.crosstab(index=housing['driveway'], 
            columns=housing['recroom']
            )
ctab


# In[48]:


test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print("P-Value =", p_value)


# In[49]:


#p-value<0.05
# we reject the H0
#driveway and recroom are may be dependent on each other


# In[51]:


df_bar = pd.melt(ctab.reset_index(),id_vars="driveway")
df_bar


# # 6. Gas Connection and Centralized Air Conditioning

# In[54]:


#categorical and categorical data 
# by Chi square test 


# In[55]:


pd.crosstab(index=housing['gashw'], 
            columns=housing['airco'],
            margins=True)


# In[56]:


test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print("P-Value =", p_value)


# In[57]:


#p-value<0.05
# we reject the H0
#driveway and recroom are may be dependent on each other


# In[62]:


df_bar = pd.melt(ctab.reset_index(),id_vars="driveway")
df_bar


# In[ ]:




