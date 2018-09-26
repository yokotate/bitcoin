import requests
import DataAccess as DA
import numpy as np
import os

class PlayGround():
    # 初期値の設定
    def __init__(self):
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        # 0 何もしない
        # 1 購入
        # 2 売却
        self.Action = [0,1,2]
        self.enable_actions = np.arange(3)
        self.env = DA.DataAccess()
        self.reset()
        
    # 初期化
    def reset(self):
        # 現在の自分の状況
        Data = self.env.SelectUserData()
        self.MyMoney = Data[0][0]
        self.MyCoin = Data[0][1]
        self.MyCoinGetValue = Data[0][2]
        self.BitcoinFlag = Data[0][3]
        # テスト用（削除してね！！）
        # res = requests.get('https://coincheck.com/api/ticker')
        # jsonData = res.json()
        # self.last = jsonData["last"]
        # self.bid  = jsonData["bid"]
        # self.ask  = jsonData["ask"]
        # self.high  = jsonData["high"]
        # self.low  = jsonData["low"]
        # self.volume  = jsonData["volume"]
        # テスト用（削除してね！！）

    # 各種仮想通貨データを取得
    def DataSet(self,last,bid,ask,high,low,volume,hour24_bid,hour24_ask,hour_bid,hour_ask):
        self.last       = last
        self.bid        = bid
        self.ask        = ask
        self.high       = high
        self.low        = low
        self.volume     = volume
        self.hour24_bid = hour24_bid
        self.hour24_ask = hour24_ask
        self.hour_bid   = hour_bid
        self.hour_ask   = hour_ask
    
    # 取れる行動をリスト形式で返す
    def EnableActionList(self):
        actlist = [0]
        # ビットコインを持っていれば売却ができる
        if self.BitcoinFlag == True:
            actlist.append(2)
        # ビットコインを持っていなければ購入ができる
        else:
            actlist.append(1)
        return actlist
    
    # 必要情報をリスト形式で返す
    def Returninfo(self):
        if self.BitcoinFlag == True:
            Flag = 1
        else:
            Flag = 0
        # 0から1の間にまとめるための正規化
        l = np.array([self.last,self.bid,self.hour24_bid,self.hour_bid,self.ask,self.hour24_ask,self.hour_ask,self.high,self.low,self.volume,self.MyMoney,self.MyCoin,self.MyCoinGetValue])
        l = l.astype(int)
        lmax = l.max()
        lmin = l.min()
        average = (l - lmin).astype(float) / (lmax - lmin).astype(float)
        average = np.append(average, np.array([Flag]))
        infolist = []
        infolist.append(average)
        return infolist
    
    # 行動の実行
    def action(self,action):
        if action == 1:
            self.BuyAction()
            self.reset()
            return 0
        elif action == 2:
            self.reset()
            return self.SellAction()
        else:
            self.NoAction()
            return self.MyMoney

    # 何もしないメソッド
    def NoAction(self):
        return 0

    # 購入するメソッド
    def BuyAction(self):
        BuyVolume = self.MyMoney / self.ask
        self.env.UpdateUserDataBuy(BuyVolume,self.MyMoney , self.bid)
        self.reset()

    # 売却するメソッド
    def SellAction(self):
        sellmoney = self.bid * self.MyCoin
        self.env.UpdateUserDataSell(sellmoney)
        self.reset()
        return sellmoney
    
    def ReturnResult(self):
        if self.MyMoney > 0:
            return self.MyMoney
        else:
            return self.bid * self.MyCoin
    
if __name__ == "__main__":
    env = PlayGround()
    env.BuyAction()

