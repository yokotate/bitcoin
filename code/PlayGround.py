import requests

class PlayGround():
    # 初期値の設定
    def __init__(self):
        # 0 何もしない
        # 1 購入
        # 2 売却
        self.Action = [0,1,2]
        self.reset()
    
    # 初期化
    def reset(self):
        res = requests.get('https://coincheck.com/api/ticker')
        jsonData = res.json()
        # 現在の自分の状況
        self.MyCoin = 0
        self.MyCoinGetValue = 0
        self.MyMoney = 0

        # 現在の取引の状況
        self.LastValue = jsonData["last"]
        self.BidValue = jsonData["bid"]
        self.AskValue = jsonData["ask"]
        self.HighValue = jsonData["high"]
        self.LowValue = jsonData["low"]
    
    # 何もしないメソッド
    def Act0(self):
        return 0

    # 購入するメソッド
    def Act1(self):
        return 1

    # 売却するメソッド
    def Act2(self):
        return 2

