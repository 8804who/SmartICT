import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('D:/공부/비교과/USG/코딩엑스AI코스/실습/data/data_smarket.csv')

data.info()
data.hist()
data.describe()
data['Year'].value_counts()
data['Direction'].value_counts()

10**np.log10((data['Today']+100)/100).sum()

X = data[['Lag1','Lag2','Lag3','Lag4','Lag5']]
y = data['Direction']

data_train = data[data['Year']<=2003]
data_test = data[data['Year']>2004]
xtrain = X[data['Year']<=2003]
xtest = X[data['Year']>2004]
ytrain = y[data['Year']<=2003]
ytest = y[data['Year']>2004]

knn = KNeighborsClassifier()
knn.fit(xtrain,ytrain)
knn.score(xtrain,ytrain)
knn.score(xtest,ytest)
yhat_knn = knn.predict(xtest)
print(confusion_matrix(ytest,yhat_knn))

param = { 'n_neighbors': [2,3,5,10,20,30,50,100,200,500] }
knn = GridSearchCV(KNeighborsClassifier(),param_grid=param)
knn.fit(xtrain,ytrain)
knn.score(xtrain,ytrain)
knn.score(xtest,ytest)
yhat_knn = knn.predict(xtest)
print(confusion_matrix(ytest,yhat_knn))

rf = RandomForestClassifier()
rf.fit(xtrain,ytrain)
rf.score(xtrain,ytrain)
rf.score(xtest,ytest)
yhat_rf = rf.predict(xtest)
confusion_matrix(ytest,yhat_rf)

param = { 'max_depth': [2,3,4,5,6,7,8,9,10,None] }
rf = GridSearchCV(RandomForestClassifier(n_estimators=500),param_grid=param)
rf.fit(xtrain,ytrain)
rf.score(xtrain,ytrain)
rf.score(xtest,ytest)
yhat_rf = rf.predict(xtest)
confusion_matrix(ytest,yhat_rf)

log_rate_naive = np.log10((data_test['Today']+100)/100)
print(10**log_rate_naive.sum())

log_rate_best = np.log10((data_test['Today']+100)/100)
log_rate_best[ ytest=='Down' ] = 0
print(10**log_rate_best.sum())

yhat = knn.predict(xtest)
log_rate_knn = np.log10((data_test['Today']+100)/100)
log_rate_knn[ yhat=='Down' ] = 0
print(10**log_rate_knn.sum())

yhat = rf.predict(xtest)
log_rate_rf = np.log10((data_test['Today']+100)/100)
log_rate_rf[ yhat=='Down' ] = 0
print(10**log_rate_rf.sum())
