from sklearn import tree
import pandas as pd

# データ全体をまとめる
iris = pd.read_csv(
    "https://raw.githubusercontent.com/pydata/pandas/master/doc/data/iris.data")

X = iris[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
Y = iris[["Name"]]
treeClf = tree.DecisionTreeClassifier(max_depth=2)
treeClf.fit(X, Y)


with open("tree.dot", "w") as f:
    f = tree.export_graphviz(treeClf, out_file=f, feature_names=[
                             "SepalLength", "SepalWidth", "PetalLength", "PetalWidth"])
