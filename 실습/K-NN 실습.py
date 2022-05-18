import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data=pd.read_csv("D:/공부/비교과/USG/코딩엑스AI코스/실습/data/Student_Performance.csv")

X = data[['math', 'reading', 'writing']]
Y = data[['preparation']]

knn_model=KNeighborsClassifier()
knn_model.fit(X,Y)

score=knn_model.score(X,Y)
print(score)