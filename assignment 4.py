import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
uploaded =files.upload()

df =pd.read_csv("indian_food.csv")
print(df)

df

#show column name
print(df.columns)

#statistical operations
print(df.describe())

#show count
print(df.count(axis=0))

#show shape of dataset
print(df.shape)

#datatypes
print(df.dtypes)

#dataframe converted into numpy array
print(df.to_numpy())

#Transpose of matrix
print(df.T)

#sorting data in reverse order axis=0=row
print(df.sort_index(axis=0,ascending=False))

#sorting data in reverse order axis=1=coulmn
print(df.sort_index(axis=1,ascending=False))

#find info of all dataset
print(df.info)

#print some specific value
print(df.loc[[1,2],['name','ingredients']])

# Slicing
print(df.loc[28:,['name','ingredients']])

#modified value to None
df['name']=None
print(df['name'])
print(df['name'].isnull())

#checking NA value
print(df.isna())

# Reindexing
reindexed=df.reindex(index=[0,1],columns=['name','ingredients'])

mising_values=["NAN","NA","---"]
df =pd.read_csv("indian_food.csv")

print(df['name'])
print(df['name'].isnull())

print(df['ingredients'])
print(df['ingredients'].isnull())

df.corr()
df.mean()
df.max()
df.describe()

from google.colab import files
uploaded =files.upload()

df1=pd.read_csv("indian_food.csv")
print(df1)

ingredients =df1["ingredients"]
x=[ ]
y=[ ]
x=list(price)
y=list(product)

#scatter plot
plt.scatter(x,y)
plt.xlabel('name->')
plt.ylabel('inredients->')
plt.title('Scatter Plot')
plt.show()
