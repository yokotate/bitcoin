
import psycopg2

class DataAccess():
    # 初期値設定
    # ここの設定は自分の環境に合わせて書き換える
    def __init__(self):
        self.path = "localhost"
        self.port = "5432"
        self.dbname = "test"
        self.user = "postgres"
        self.password = "password"

    # データベース接続
    # プライベート関数
    # カーソルとコネクションを返します。
    def __ConectToDB(self):
        conText = "host={} port={} dbname={} user={} password={}"
        conText = conText.format(self.path,self.port,self.dbname,self.user,self.password)
        connection = psycopg2.connect(conText)
        connection.get_backend_pid()
        cur = connection.cursor()
        return cur,connection

    # BTC_VALUEテーブルに対するInsertを実行します。
    # 6つのデータが必要です。
    def InsertToBTC_VALUE(self,last,bid,ask,high,low,volume):
        cur,connection = self.__ConectToDB()
        sql  = "INSERT INTO BTC_VALUE (last_val,bid_val,ask_val,high_val,low_val,volume_val) VALUES({},{},{},{},{},{})"
        sql  = sql.format(last,bid,ask,high,low,volume)
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
    
    # BTC_VALUEテーブルからデータを全て取得し、List形で返す
    # トレーニング用の関数
    def SelectBTC_VALUE(self):
        BtcList = []
        cur,connection = self.__ConectToDB()
        sql = "SELECT * FROM BTC_VALUE"
        cur.execute(sql)
        # 取得したデータをList形に変換
        for row in cur:
            BtcList.append(row)
        cur.close()
        connection.close()
        return BtcList
    
    def SelectUserData(self):
        userdata = []
        try:
            cur,connection = self.__ConectToDB()
            sql = "SELECT * FROM USERDATA"
            cur.execute(sql)
            for row in cur:
                userdata.append(row)
            cur.close()
            connection.close()
            return userdata
        except:
            return userdata
   
    # BTCを買った際にユーザーデータの更新を行う
    def UpdateUserDataBuy(self,volume,value):
        try:
            cur,connection = self.__ConectToDB()
            sql = "UPDATE USERDATA SET money = 0, bitcoin = {}, bitcoinbuyvalue = {}, BitCoinFlag = TRUE"
            sql = sql.format(volume,value)
            cur.execute(sql)
            connection.commit()
            cur.close()
            connection.close()
            return True
        except:
            return False

    # BTCを売った際にユーザーデータの更新を行う
    def UpdateUserDataSell(self,money):
        try:
            cur,connection = self.__ConectToDB()
            sql = "UPDATE USERDATA SET money = {}, bitcoin = 0, bitcoinbuyvalue = 0, BitCoinFlag = FALSE"
            sql = sql.format(money)
            cur.execute(sql)
            connection.commit()
            cur.close()
            connection.close()
            return True
        except:
            return False
    
    def TrainDataSet(self):
        try:
            cur,connection = self.__ConectToDB()
            sql = "UPDATE USERDATA SET money = 10000, bitcoin = 0, bitcoinbuyvalue = 0, BitCoinFlag = FALSE"
            cur.execute(sql)
            connection.commit()
            cur.close()
            connection.close()
            return True
        except:
            return False


        
        
if __name__ == "__main__":
    env = DataAccess()
    env.SelectBTC_VALUE()

    