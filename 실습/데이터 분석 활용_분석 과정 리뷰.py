import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("D:/공부/비교과/USG/코딩엑스AI코스/실습/data/Student_Performance.csv")
print(data.isna().sum())
print(data.describe())

data.hist()
plt.show()