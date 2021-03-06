
# 単回帰分析
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyper
from sklearn import linear_model

# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")

# 品種ごとにまとめる
setosa = iris[iris["Name"] == "Iris-setosa"]
LinearRegr = linear_model.LinearRegression()
X = setosa[["SepalLength", "PetalLength", "PetalWidth"]]
Y = setosa[["SepalWidth"]]
LinearRegr.fit(X, Y)
print(LinearRegr.score(X, Y))  # 決定係数

r = pyper.R(use_pandas='True')
r.assign('data', iris)  # pandas で読み込んだデータを R に渡す
# 重回帰分析を行う
r('rlm <- lm(Sepal.Width ~ Sepal.Length+Petal.Length+Petal.Width,data=iris)')
print(r('summary(rlm)'))  # 分析結果の出力

#plt.scatter(X, Y, color="black")
#
#px = np.arange(X.min()[0], X.max()[0], 0.01)[:, np.newaxis]
#py = LinearRegr.predict(px)
#plt.plot(px, py, color="blue", linewidth=3)
# plt.xlabel("SepalLength")
# plt.ylabel("SepalWidth")
# plt.show()
# print(LinearRegr.coef_)  # 回帰係数
# print(LinearRegr.intercept_)  # 切片
#
# print(LinearRegr.score(X, Y))  # 決定係数
