import DataAccess as da
import numpy as np
import sys
import matplotlib.pyplot as plt

# 平均集計用変数
hour24_bid = np.array([])
hour24_ask = np.array([])
hour_bid   = np.array([])
hour_ask   = np.array([])

# DBアクセス
daenv = da.DataAccess()
data = daenv.SelectBTC_VALUE()

# データ収集用
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

# データ収集開始
for row in data:
    i = i + 1
    if i <= 1439:
        continue
    # 平均値算出用データ集計
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


# 描画設定
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# 描画データ設定
ax.plot(li, l24bid, label = "買値（24時間平均）")
ax.plot(li, lbid,   label = "買値（1時間平均）")
ax.plot(li, bid,    label = "買値（現在）")
ax.plot(li, l24ask, label = "売値（24時間平均）")
ax.plot(li, lask,   label = "売値（1時間平均）")
ax.plot(li, ask,    label = "売値（現在）")
ax.plot(li, lh,     label = "最高売値（過去24時間）")
ax.plot(li, ll,     label = "最低買値（過去24時間）")
# ラベル表示
plt.legend()
# タイトル
plt.title("ビットコイン価格推移")
# 軸ラベル表示
plt.xlabel("時間")
plt.ylabel("価格")
# 描画
plt.show()
