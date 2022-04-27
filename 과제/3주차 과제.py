#가
import pandas as pd
data=pd.read_csv('./public/csv/practice01.csv')
data=pd.DataFrame(d)

#나
print(data.head())

#다
print(data[5:9])

#라
print(data.columns)

#마
print(data.iloc[5:8,1:3])

#바
print(data[data.gender=='male'])