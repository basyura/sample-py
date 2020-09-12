#!python
# -*- coding: utf-8 -*-
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import datetime

colors = ["blue", "red", "magenta", "orange", "green",
          "cyan", "brown", "gold", "darkgray", "skyblue"]
fields = [["P700", "70%"], ["P900", "90%"]]


def main():
    labels = list(map(lambda x: x[0], fields))
    # fetch data and construct dictionary which mapped with user
    dic = fetch(labels)
    if dic is None:
        print("no record")
        return
    generate(dic)


def generate(dic):
    labeldate = to_labeldate(dic)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

    count = 0
    for user in dic:
        npary = np.array(dic[user])
        # 日付列を取得
        x = pd.to_datetime(npary[:, 1])
        # npary
        # [['A' '2020-07-13' '12939' '633']
        #  ['A' '2020-07-20' '12800' '649']
        #  ['A' '2020-07-27' '13291' '630']
        #  ['A' '2020-08-10'  '4676' '433']
        #  ['A' '2020-08-17' '13352' '658']
        #  ['A' '2020-08-24' '13105' '630']]
        # npary[:, i + 3]
        # ['633' '649' '630' '433' '658' '630']
        for i in range(len(fields)):
            # user label
            ax.text(labeldate, int(npary[0][i+3]), user,
                    horizontalalignment='right', color=colors[count])
            ax.plot(x, np.array(npary[:, i+3], dtype=np.int64),
                    marker="o",
                    label=user + ":" + fields[i][1],
                    color=colors[count])

            # 行ごと x 軸ごとに値をプロット
            for r in npary:
                ax.text(r[1], int(r[i+3]) + 10, r[i+3])

        count += 1

    plt.title("title")
    plt.legend()
    plt.savefig("Py.png")


def fetch(fields):

    rows = []
    with open("./multi_line.tsv") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            rows.append(row)
    # error (no record)
    if len(rows) == 0:
        return None
    # ユーザーごとに分ける
    dic = {}
    for r in rows:
        user = r[0]
        v = dic.get(user)
        if v is None:
            v = []
            dic[user] = v
        v.append(r)

    return dic


def to_labeldate(dic):
    dates = []
    for d in dic.values():
        for v in d:
            dates.append(v[1])
    dates.sort()
    date = dates[0]
    # datetime に変換して前日を算出してから string に戻す
    date = (datetime.datetime.strptime(
        date, "%Y-%m-%d") - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    return date


if __name__ == '__main__':
    main()
