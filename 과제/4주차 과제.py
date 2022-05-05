#가
import pandas as pd
data = pd.read_csv('./public/csv/practice01.csv')

#나
data=data.dropna()
print(data)

#다
print(data['gender'].value_counts())

#라
print(data.describe())

#마
print(data[['age', 'price', 'grade', 'time']].corr())

#바
print(data.groupby(data['gender']).max())

