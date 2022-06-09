from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import pandas as pd

#가
data = pd.read_csv('D:/공부/비교과/USG/코딩엑스AI코스/실습/data/wine_data.csv')
print(data.head())

#나
y=data['style']
X=data[['total_sulfur_dioxide', 'chlorides', 'volatile_acidity', 'alcohol']]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

#다
sm=SMOTE(random_state=42)
X_sampled, y_sampled = sm.fit_resample(X_train, y_train)

#라
param_grid={
    'n_estimators': [100, 150, 200, 250],
    'max_depth': [None, 3, 6 ,9],
}
model_rf=RandomForestClassifier()
grid_search=GridSearchCV(estimator=model_rf, param_grid=param_grid, scoring='accuracy')
grid_search.fit(X_sampled, y_sampled)

#마
y_pred = grid_search.predict(X_test)
print("F1-Score:", f1_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test,y_pred))