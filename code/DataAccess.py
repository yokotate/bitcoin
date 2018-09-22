
import psycopg2

class DataAccess():
    # init
    # Connection info
    def __init__(self):
        self.path = "localhost"
        self.port = "5432"
        self.dbname = "dbname"
        self.user = "postgres"
        self.password = "pass"

    # データベース接続
    # カーソルとコネクションを返します。
    def ConectToDB(self):
        conText = "host={} port={} dbname={} user={} password={}"
        conText = conText.format(self.path,self.port,self.dbname,self.user,self.password)
        connection = psycopg2.connect(conText)
        connection.get_backend_pid()
        print(connection)
        cur = connection.cursor()
        return cur,connection

    # BTC_VALUEテーブルに対するInsertを実行します。
    # 6つのデータが必要です。
    def InsertToBTC_VALUE(self,last,bid,ask,high,low,volume):
        cur,connection = self.ConectToDB()
        sql  = "INSERT INTO BTC_VALUE (last_val,bid_val,ask_val,high_val,low_val,volume_val) VALUES({},{},{},{},{},{})"
        sql  = sql.format(last,bid,ask,high,low,volume)
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
    
    def SelectBTC_VALUE(self):
        cur,connection = self.ConectToDB()
        sql = ""
        

if __name__ == "__main__":
    env = DataAccess()
    env.InsertToBTC_VALUE