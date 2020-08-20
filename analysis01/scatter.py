#!python
import sklearn
import matplotlib.pyplot as plt
import scipy as sp
import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix

# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")
# 品種ごとにまとめる
setosa = iris[iris["Name"] == "Iris-setosa"]

# 散布図
plt.scatter(setosa["SepalLength"], setosa["SepalWidth"])
plt.xlabel("SelapLength")
plt.ylabel("SepalWidth")
plt.show()

# 相関係数
corr = np.corrcoef(setosa["SepalLength"], setosa["SepalWidth"])
print(corr[0, 1])  # => 0.746

# 散布図行列
pd.plotting.scatter_matrix(setosa)
plt.tight_layout()
plt.show()
