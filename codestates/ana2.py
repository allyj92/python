# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:22:36 2024

@author: tjrwn
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv('C:\\Users\\tjrwn\\Desktop\\df_funnel.csv');
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)

df['datetime']  = pd.to_datetime(df['datetime'])


print(df.isna().sum())


df['actiontype'] = df['actiontype'].map({'OPEN': 1, 'CLOSE': 0})
df['actiontype'] = df['actiontype'].fillna(0)

df['actiontype'] = df['actiontype'].astype(int)
print(df.dtypes)

df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
print(df.head())

df = df.drop(columns = ['datetime']);
print(df.dtypes)



# ismydoc
df['ismydoc'] = df['ismydoc'].map({'NoView': 0, "View": 1})
df['ismydoc'] = df['ismydoc'].astype(int)

import matplotlib.pyplot as plt

corr_matrix = df[['actiontype', 'year', 'month', 'day']].corr()
print(corr_matrix)




import pandas as pd
import matplotlib.pyplot as plt

df.groupby('day')['actiontype'].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(12, 6))
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()


df2 = pd.read_csv('C:\\Users\\tjrwn\\Desktop\\kuiData.csv');
print(df2.head())
print(df2.columns)
print(df2.shape)
print(df2.info())

print(df2.describe())
print(df2.dtypes)
df2['countryCode'].fillna('Unknown', inplace=True)
print(df2.isnull().sum())

from sklearn.preprocessing import LabelEncoder

