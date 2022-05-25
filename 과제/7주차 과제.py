import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

#가
data=pd.read_csv('/data/Student_Performance.csv')

#나
X=data[['math', 'reading', 'writing']]

#다
y=data['preparation']

#마
Knn_model=KNeighborsClassifier()
Knn_model.fit(X, y)
print(Knn_model.score(X, y))

#바
DecisionTreeModel=DecisionTreeClassifier(max_depth=3)
DecisionTreeModel.fit(X,y)
print(DecisionTreeModel.score(X,y))