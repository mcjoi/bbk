import pandas as pd
import numpy as np


from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



df  = pd.read_csv('C:\\Users\\bong\Desktop\\bbk\\mtcars.csv')

# 한개의 데이터프레임에서 모델에 사용할 데이터만 분리함.
X = df.drop(columns=['model', 'am'])
y = df['am']


# 변수 분류
numeric_features = ['mpg', 'disp', 'hp', 'drat', 'wt', 'qsec']
categorical_features = ['cyl', 'vs', 'gear', 'carb']

# 전처리
# 라벨인코더는 한번에 하나씩의 컬럼만 처리가 가능하다.
scaler = StandardScaler()
X[numeric_features] = scaler.fit_transform(X[numeric_features])

lb = LabelEncoder()
# X[categorical_features] = lb.fit_transform(X[categorical_features])

for col1 in categorical_features :
    X[col1] = lb.fit_transform(X[col1])
    
# 쪼개기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# print(X_train.shape, X_test.shape, y_train.shape)


# 모델
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

#이거 드럽게 안외워짐.
y_pred = rf.predict(X_test)


# y_test를 먼저 넣어줘야 한다.
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))





