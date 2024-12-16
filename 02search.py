import data as d

# 
df02 = d.df_mtcars.copy()

# change index number from 1
df02.index += 1

# 1,2,3번 인덱스와 label index 번호가 다름에 주의!
print(df02.iloc[[1,2,3],:])
print(df02.loc[[1,2,3],:])