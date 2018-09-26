import PlayGround as pg
import DataAccess as da
import numpy as np
import os,sys
from dqn_agent import DQNAgent

# ログファイル設定
import logging
import datetime
logger = logging.getLogger('LoggingTest')
logger.setLevel(10)
now = datetime.datetime.now()
a = 'log/test_{0:%Y%m%d}.log'
a = a.format(now)
print(a)
fh = logging.FileHandler(a)
logger.addHandler(fh)
sh = logging.StreamHandler()
logger.addHandler(sh)
formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

if __name__ == "__main__":
    # parameters
    n_epochs = 1000
    TestDataNum = 200

    pgenv = pg.PlayGround()
    daenv = da.DataAccess()
    data = daenv.SelectBTC_VALUE()
    agent = DQNAgent(pgenv.enable_actions,pgenv.name,14)

    averagelist = [10000]

    # 決められた回数実行する
    for e in range(n_epochs):
        # 初期化
        pgenv.reset()
        i = 0
        length = len(data)
        # 初期金額を保存
        InitBuyMoney = pgenv.MyMoney

        # 1時間及び24時間平均算出用変数
        hour24_bid = np.array([])
        hour24_ask = np.array([])
        hour_bid   = np.array([])
        hour_ask   = np.array([])

        # ランダムデータトレーニング
        # rnd = int(np.random.rand() * (len(data) - 1441 - TestDataNum))
        # rndData = np.array(data[rnd:rnd + 1440 + TestDataNum])

        # トレーニングデータの作成
        daenv.TrainDataSet()

        # データ個数分トレーニングを実行する
        for row in data:
            i = i + 1
            if i <= 1439:
                continue
            hour24_bid = np.array(data[i - 1440:i])[:,2]
            hour24_ask = np.array(data[i - 1440:i])[:,3]
            hour_bid   = np.array(data[i - 60:i])[:,2]
            hour_ask   = np.array(data[i - 60:i])[:,3]
            
            # データセット
            pgenv.DataSet(row[1], row[2], row[3], row[4], row[5], row[6], np.average(hour24_bid), np.average(hour24_ask), np.average(hour_bid), np.average(hour_ask))

            # 行動実行前データ
            enable_actions = pgenv.EnableActionList()
            infolist = pgenv.Returninfo()
            BitCoinFlag = pgenv.BitcoinFlag

            # 実行処理
            action = agent.select_action(infolist,enable_actions,agent.exploration)
            # 取得時現金を取得
            MyMoney = pgenv.MyMoney

            pgenv.action(action)
            if action == 0:
                act = "No Action"
            elif action == 1:
                act = "Buy"
            elif action == 2:
                act = "Sell"

            # 行動実行後データ
            after_enable_actions = pgenv.EnableActionList()
            after_infolist = pgenv.Returninfo()
            after_BitCoinFlag = pgenv.BitcoinFlag

            result = pgenv.ReturnResult()
            
            reword = 0
            if action == 2:
                bairitu = result / MyMoney
                if 1.0 <= bairitu:
                    reword = bairitu
                    logger.log(100,"GREATE SUCCESS!!!")
                agent.store_experience(infolist,enable_actions,action,reword,after_infolist,after_enable_actions,True)
            else:
                agent.store_experience(infolist,enable_actions,action,reword,after_infolist,after_enable_actions,False)
                agent.experience_replay()
            logger.log(10, "epochs:%d data:%d Result:%d profit:%d act:%s" % (e, i - 1439, pgenv.ReturnResult(), pgenv.ReturnResult() - InitBuyMoney, act))
        logger.log(20, "END Epochs:%d Result:%d profit:%d" % (e, pgenv.ReturnResult(), pgenv.ReturnResult() - InitBuyMoney)) 
        
    agent.save_model()


