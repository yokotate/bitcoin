import DataAccess as da
import numpy as np
import sys
import matplotlib.pyplot as plt

hour24_bid = np.array([])
hour24_ask = np.array([])
hour_bid   = np.array([])
hour_ask   = np.array([])

daenv = da.DataAccess()
data = daenv.SelectBTC_VALUE()
i=0
l24ask = []
ask = []
l24bid = []
bid = []
lask   = []
lbid   = []
lh =[]
ll = []
li = []
# データ個数分トレーニングを実行する
for row in data:
    i = i + 1
    if i <= 1439:
        continue
    hour24_bid = np.array(data[i - 1440:i])[:,2]
    hour24_ask = np.array(data[i - 1440:i])[:,3]
    hour_bid   = np.array(data[i - 60:i])[:,2]
    hour_ask   = np.array(data[i - 60:i])[:,3]

    # 描画用データ収集
    l24bid.append(np.average(hour24_bid))
    l24ask.append(np.average(hour24_ask))
    lbid.append(np.average(hour_bid))
    lask.append(np.average(hour_ask))
    bid.append(row[2])
    ask.append(row[3])
    lh.append(row[4])
    ll.append(row[5])
    li.append(i -1440)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(li,l24bid)
ax.plot(li,l24ask)
ax.plot(li,bid)
ax.plot(li,ask)
ax.plot(li,lask)
ax.plot(li,lbid)
ax.plot(li,lh)
ax.plot(li,ll)
plt.show()
