
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyper
from sklearn import linear_model

# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")


# ロジスティック回帰モデル
usedata = np.logical_or(iris["Name"] == "Iris-setosa",
                        iris["Name"] == "Iris-virginica")
setosa_virginica = iris[usedata]
X = setosa_virginica[["SepalLength", "SepalWidth"]]
Y = setosa_virginica["Iris-setosa"]
LogRegr = sklearn.linear_model.LogisticRegression(C=1.0)
LogRegr.fit(X, Y)
print(LogRegr.coef_)
# 偏回帰係数
print(LogRegr.intercept_)
# 切片
print(pd.crosstab(Y, LogRegr.predict(x)))  # 予測結果


# usedata = np.logical_or(iris["Name"] == "Iris-setosa",
#                         iris["Name"] == "Iris-virginica")
# setosa_virginica = iris[usedata]
# X = setosa_virginica[["SepalLength", "SepalWidth"]]
# Y = setosa_virginica["Iris-setosa"]

# LongRegr = sklearn.linear_model.LogisticRegression(C=1.0)
# LongRegr.fit(X, Y)
