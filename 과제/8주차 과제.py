from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.cluster import KMeans
import pandas as pd
#가
data=pd.read_csv('/data/Student_Performance.csv')

#나
X=data[['math','reading','writing']]
y=data['preparation']

#다
rf_model=RandomForestClassifier()
rf_model.fit(X, y)
print(rf_model.score(X, y))

#라
MLP_model=MLPClassifier()
MLP_model.fit(X, y)
print(MLP_model.score(X, y))

#마
data2=pd.read_csv('/data/iris.csv')
X = data2.drop(columns=['caseno','Species'])

#바
K_means_model=KMeans(n_clusters=3)
K_means_model.fit(X)
data2['cluster']=K_means_model.labels_
print(data2)