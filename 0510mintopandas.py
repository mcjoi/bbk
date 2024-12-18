

import pandas as pd
import numpy as np


s = pd.Series([1,3,5,np.nan,6,8])

# print(s)


# generate dataframe
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
# print(df)






df2 = pd.DataFrame({
    "a" : 1.0,
    "b" : pd.Timestamp("20130102"),
    "c" : pd.Series(1, index=list(range(4)), dtype="float32"),
    "d" : np.array([3] * 4, dtype="int32"), 
    "e" : pd.Categorical(["test", "train", "test", "train"]),
    "f" : "foo",
})


# print(df2)
# print(df2.info())
# print(df2.dtypes)


#### viewing data

import data as d
df3 = d.df_iris.copy()


# print(df.head())
# print(df.tail())

# print(df.index)
# print(len(df))

# print(df.to_numpy())


# Numpy arrays have one dtype for the entire array while pandas DataFrame have one dtype per column.
# when you call to_numpy, pandas will find the Numpy dtype that can hold all of the types in the Dataframe.
# print(df2.to_numpy().dtype) # object


# quick summary of data
print(df.shape)
print(df.info())
print(df.describe())

# Transposing your data
# print(df.T)

# sort by an index
# print(df.sort_index(axis=1, ascending=False)) # axis = 1 means column, column names
# print(df.sort_index(axis=0, ascending=False)) # axis = 0 means row, indexed variable

# sort by values
# print(df.sort_values(by="B"))













