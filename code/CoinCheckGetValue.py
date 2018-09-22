# ビットコインで価格を取得してPostgreSQLに接続して保存するまで

import requests
import psycopg2
class CoinCheckGetCValue():
    # coincheck で取得
    res = requests.get('https://coincheck.com/api/ticker')
    jsonData = res.json()
    # last 直近売買
    # bid 買値
    # ask 売値
    # high  24時間での最高取引価格
    # low  24時間での最安取引価格
    # volume 24時間での取引量 
    connection = psycopg2.connect("host=localhost port=5432 dbname=test user=postgres password=k_yokose1330076")
    # connection = psycopg2.connect("host=localhost port=5432 dbname=DBNAME user=USER password=PASSWORD")
    connection.get_backend_pid()

    cur = connection.cursor()

    last = jsonData["last"]
    bid  = jsonData["bid"]
    ask  = jsonData["ask"]
    high  = jsonData["high"]
    low  = jsonData["low"]
    volume  = jsonData["volume"]
    
    sql  = "INSERT INTO BTC_VALUE (last_val,bid_val,ask_val,high_val,low_val,volume_val)"
    sql += " VALUES(" + str(last) + "," + str(bid) + "," + str(ask) +  "," + str(high) + "," + str(low) + "," + str(volume) + ")"

    cur.execute(sql)
    connection.commit()
    # print(jsonData)

if __name__ == "__main__":
    env = CoinCheckGetCValue()
