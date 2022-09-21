import pandas as pd 
import numpy as np 
df = pd.read_csv('articles.csv')
df = df.sort_values(['total_events'], ascending=[False]) 
output = df[['total_events']].head(100).values.tolist()
print(output)