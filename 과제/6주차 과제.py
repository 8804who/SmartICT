import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#가
data=pd.read_csv('/data/iris.csv')

#나
del data['caseno']

#다
plt.plot(data['PetalWidth'])
plt.show()

#라
data.corr()
sns.heatmap(data.corr(), annot=True)
plt.show()

#마
plt.hist(data['PetalLength'])
plt.title("PetalLength")
plt.show()

#바
plt.hist(data['PetalLength'], color=['red'])
plt.title("PetalLength")
plt.show()
