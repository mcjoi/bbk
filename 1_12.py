import pandas as pd


# 주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구해보세요 
# (단, 100%가 넘는 접종률 제거, 소수 첫째자리까지 출력)

# - 데이터셋 : ../input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv


df = pd.read_csv('covid-vaccination-vs-death_ratio.csv')



df2 = df[['country', 'ratio']]

df3 = df2.groupby(['country']).sum()

df3 = df3[df3['ratio'] <= 100]
df3_sorted = df3.sort_values('ratio', ascending=False)

print(df3_sorted.head(10).mean())
print(df3_sorted.tail(10).mean())

# 'Unnamed: 0', 'country', 'iso_code', 'date', 'total_vaccinations',
# 'people_vaccinated', 'people_fully_vaccinated', 'New_deaths',
# 'population', 'ratio'