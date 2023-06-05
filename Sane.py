import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv(r"C:\Users\pgdbda\Desktop\Anjali\Advanced stat\data set\iris.csv")
print(df)


g=sns.FacetGrid(df,col="Species")
g.map(sns.histplot,"Petal.Length")
plt.show()



sns