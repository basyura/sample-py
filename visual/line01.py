import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# 折れ線グラフを出力
records = [
    ["2020-07/01 09:00:00", 100, 50],
    ["2020-07/01 10:00:00", 200, 100],
    ["2020-07/01 11:00:00", 350, 150],
    ["2020-07/01 12:00:00", 450, 200],
]

npary = np.array(records)
x = pd.to_datetime(npary[:, 0])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, np.array(npary[:, 1], dtype=np.int64))
ax.plot(x, np.array(npary[:, 2], dtype=np.int64))

ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.set_ylim([0, 500])

plt.savefig('Py.png')
