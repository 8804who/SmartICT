#가
import pandas as pd
iris=pd.read_csv('/content/iris.csv')

#나
import matplotlib.pyplot as plt
plt.hist(data['PetalLength'])

#다
count=data['Species'].value_counts()
name=count.index
plt.pie(count, labels=name)
plt.show()

#라
import seaborn as sns
sns.pairplot(data)
plt.show()

#마
data.groupby('Species').mean()

#바
data_dummy=pd.get_dummies(data)
data_dummy