
# 単回帰分析
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 import pyper
from sklearn import linear_model

# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")

# カテゴリデータを数値として扱うため
# 品種ごとに該当する要素に 1、該当しない場合は 0 を入れる。
dummies = pd.get_dummies(iris["Name"])
iris = pd.concat([iris, dummies], axis=1)

LinerRegr = linear_model.LinearRegression()
X = iris[["Iris-virginica", "Iris-versicolor"]]
Y = iris[["SepalLength"]]
LinerRegr.fit(X, Y)
print(LinerRegr.coef_)
print(LinerRegr.intercept_)
