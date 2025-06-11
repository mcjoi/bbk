import pandas as pd


df = pd.read_csv('C:\\Users\\bong\\Desktop\\bbk\\basic1.csv')

# 주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오


# print(df.head())


target = ['f5']

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
df['f5'] = sc.fit_transform(df[target])

print(df['f5'].median())
