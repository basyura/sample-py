#!python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster
# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")

X = iris[["SepalLength", "SepalWidth"]]
kmeansCls = cluster.KMeans(n_clusters=3, random_state=71)
kmeansCls.fit(X)
print(kmeansCls.predict(X))


def category2int(x):
    category = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
    return category[x]


def f(x): return category2int(x)


Y = iris["Name"].map(f)
xMin = X["SepalLength"].min()
xMax = X["SepalLength"].max()
yMin = X["SepalWidth"].min()
yMax = X["SepalWidth"].max()
xx, yy = np.meshgrid(np.arange(xMin, xMax, 0.01),
                     np.arange(yMin, yMax, 0.01))
Z = kmeansCls.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
plt.scatter(X["SepalLength"].ix[Y.values == 0],
            X["SepalWidth"].ix[Y.values == 0], marker="o", c="black")
plt.scatter(X["SepalLength"].ix[Y.values == 1],
            X["SepalWidth"].ix[Y.values == 1], marker="o", c="black")
plt.scatter(X["SepalLength"].ix[Y.values == 2],
            X["SepalWidth"].ix[Y.values == 2], marker="o", c="black")
