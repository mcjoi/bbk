import data as d
df03 = d.df_iris.copy()

# select column : 0, 4
df04 = df03.iloc[:, 0:100]

# rename specific column
df04.rename(columns={'variety': 'Variety'}, inplace=True)

print(df04.head(10))

# select column named
print(df04.loc[:,['Variety', 'sepal.length']].head(10))






