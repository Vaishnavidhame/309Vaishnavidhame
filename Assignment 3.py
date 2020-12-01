import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from google.colab import files
uploaded=files.upload()

dataset=pd.read_csv("indian_food.csv")
dataset 

dataset.plot.bar()
plt.title("bar plot")
Text(0.5, 1.0, 'bar plot')

dataset.plot.hist()
plt.title("histogram graph")
Text(0.5, 1.0, 'histogram graph')

dataset. plot.line()
plt.title("line garph")
Text(0.5, 1.0, 'line garph')


