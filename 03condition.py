import data as d

# 
df03 = d.df_iris.copy()

print(df03.shape)
print(df03.columns)

print(df03.describe())


#--
# print(df03.info())
# print(df03['sepal.length'].describe())
# print(df03['sepal.length'].mean())
# print(df03.groupby(by='variety').mean())

# 조건설정
# cond1 = df03['variety'] == 'Versicolor' 
# cond2 = df03['petal.width'] >= 0.2

# 조건을 만족하는 신규 데이터프레임
# df04 = df03[(cond1) | (cond2)]

# 정렬
# df05 = df04.sort_values(ascending=False, by='sepal.length')

# 상위 데이터만 남긴 신규 데이터 프레임
# print(len(df05))
# print(int(len(df05) * 0.1))
# df06 = df05.head(int(len(df05) * 0.1))
# print(df06)



