# ビットコインで価格を取得してPostgreSQLに接続して保存するまで

import requests
import psycopg2

# coincheck で取得
res = requests.get('https://coincheck.com/api/ticker')
jsonData = res.json()
# last 直近売買
# bid 買値
# ask 売値
# high  24時間での最高取引価格
# low  24時間での最安取引価格
# volume 24時間での取引量 
connection = psycopg2.connect("host=localhost port=5432 dbname=DBNAME user=USERID password=PASSWORD")
connection.get_backend_pid()

cur = connection.cursor()

last = jsonData["last"]
sql ="INSERT INTO CC VALUE(" + last + ")"

cur.execute(sql)
cur.fetchone()
# print(jsonData)