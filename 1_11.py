import pandas as pd


df = pd.read_csv('C:\\Users\\bong\\Desktop\\bbk\\basic1.csv')

# min-max스케일링 기준 상하위 5% 구하기
# 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오

# - 데이터셋 : basic1.csv

from sklearn.preprocessing import minmax_scale

target = ['f5']

df['f5']  = minmax_scale(df[target])

df.sort_values('f5', inplace=True, ascending=False)

upper = df['f5'].quantile(0.95)
lower = df['f5'].quantile(0.05)

print(upper, lower, upper + lower)









