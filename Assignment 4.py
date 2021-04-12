import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded =files.upload()

df =pd.read_excel("job_seeker_data.xlsx")
print(df)

#show column name
print(df.columns)

#show index
print(df.index)

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
print(df.loc[[1,2],['Year','Engineering Diploma Holders']])

# Slicing
print(df.loc[28:,['Year','Engineering Diploma Holders']])

#modified value to None
df['Year']=None
print(df['Year'])
print(df['Year'].isnull())

#checking NA value
print(df.isna())

# Reindexing
reindexed=df.reindex(index=[0,1],columns=['Year','Graduates-Total'])

from google.colab import files
uploaded =files.upload()

df1=pd.read_excel("selling_product.xlsx")
print(df1)

product =df1["Device"]
price =df1["Price"]

x=[ ]
y=[ ]
x=list(price)
y=list(product)

#scatter plot
plt.scatter(x,y)
plt.xlabel('Price->')
plt.ylabel('Product->')
plt.title('Scatter Plot')
plt.show()

#pie plot
plt.pie(x,labels=y,autopct='%.2f%%')
