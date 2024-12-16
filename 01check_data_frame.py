import data as d


# 
df01 = d.df_mtcars.copy()


# row * col
#print(df01.shape)

# null check
#print(df01.info())

# columns name
#print(df01.columns)


#integer location - read by index number
#print(df01.iloc[[0,5],[0,1]])


# location - read  by name of row/column
cond1 = [0]
print(df01.loc[cond1,["cyl", "model"]])





