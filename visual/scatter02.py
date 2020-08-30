import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# matplotlib.pyplot.scatter(
#  x, y, s=20, c=None, marker='o', cmap=None, norm=None,
#  vmin=None, vmax=None, alpha=None, linewidths=None,
#  verts=None, edgecolors=None, hold=None, data=None,
#  **kwargs)


def main():

    # データ読み込み
    df = pd.read_table('~/Desktop/sample.tsv')
    # 軸とデータ
    x = pd.to_datetime(df['end'])
    y = df['elapsed']

    fig = plt.figure()
    #fig = plt.figure(figsize=(20, 20))
    ax = fig.add_subplot(1, 1, 1)
    # s: マーカーサイズ
    ax.scatter(x, y, s=1)
    # ラベル
    ax.set_title('first scatter plot')
    ax.set_ylabel("elapsed [ms]")
    # y 軸の最大値
    ax.set_ylim([0, 60000])
    # メモリの表示間隔
    #daysLoc = mdates.HourLocator(byhour=None, interval=1, tz=None)
    # ax.xaxis.set_major_locator(daysLoc)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    # 画像として保存
    plt.savefig("Py.png")


if __name__ == '__main__':
    main()
