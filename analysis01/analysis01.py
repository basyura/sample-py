#!python
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import sklearn
# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")
# 品種ごとにまとめる
setosa = iris[iris["Name"] == "Iris-setosa"]
versicolor = iris[iris["Name"] == "Iris-versicolor"]
virginica = iris[iris["Name"] == "Iris-virginica"]

# 品種ごとの平均値
print(iris.groupby("Name").mean())

plt.figure()
# 品種全てでグラフ化
# plt.hist(iris["SepalLength"])
# setosa 品種でグラフ化
plt.hist(setosa["SepalLength"])
plt.xlabel("SepalLength")
plt.ylabel("Freq")
plt.show()


data = [setosa["SepalLength"],
        versicolor["SepalLength"], virginica["SepalLength"]]
plt.figure()
plt.boxplot(data, sym="k.")
plt.xlabel("Name")
plt.ylabel("SepalLength")
ax = plt.gca()
plt.setp(ax, xticklabels=["setosa", "versicolor", "virginica"])
plt.show()
