# ビットコインで価格を取得してPostgreSQLに接続して保存するまで

import requests
import psycopg2
import DataAccess as da

class CoinCheckGetCValue():
    # coincheck で取得
    def InsBTC_VALUE(self):
        res = requests.get('https://coincheck.com/api/ticker')
        jsonData = res.json()
        # last 直近売買
        # bid 買値
        # ask 売値
        # high  24時間での最高取引価格
        # low  24時間での最安取引価格
        # volume 24時間での取引量 
        last = jsonData["last"]
        bid  = jsonData["bid"]
        ask  = jsonData["ask"]
        high  = jsonData["high"]
        low  = jsonData["low"]
        volume  = jsonData["volume"]
        
        # 取得したデータを保存用プログラムに投げる
        env = da.DataAccess()
        env.InsertToBTC_VALUE(last,bid,ask,high,low,volume)

if __name__ == "__main__":
    env = CoinCheckGetCValue()
    env.InsBTC_VALUE()
