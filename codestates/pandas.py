# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv('C:\\Users\\tjrwn\\Desktop\\archive (1)\\train.csv');
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.isnull().sum())
#age컬럼의 평균 계산 방법?
df['Age'].fillna(int(df['Age'].mean()), inplace=True)
print(df.isnull().sum())
df = df.drop("Cabin",axis=1,inplace=True)

#최빈값
max_count = df['Embarked'].mode()[0]
df['Embarked'].fillna(max_count, inplace= True)
print(df.info)

df.groupby('Pclass').sum()['Survived']

