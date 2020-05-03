import pandas as pd
import numpy as np
import math


sample_csv = pd.read_csv("sample.csv", index_col=0)
read_lots = pd.read_csv("products.csv", index_col=0)


# today_csvからお届け本数の取得
class order():
    def __init__(self, name, shop):
        self.name = name
        self.shop = shop
    # その日のお届け総本数
    def Tnum(self):
        if self.shop == "由利本荘店":
            today_csv = pd.read_csv("発注リスト2.csv", encoding="cp932", header=1, index_col=5)
        else:
            today_csv = pd.read_csv("発注リスト.csv", encoding="cp932", header=1, index_col=5)
        try:
            n = today_csv[today_csv["支店名"] == self.shop]
            a = n.loc[self.name, "数量"]
            return a
        except:
            return 0




# products.csvからデータを取得する
class products_c():
    def __init__(self, name):
        self.name = name
# コードを取得する
    def Code(self):
        a = read_lots.loc[self.name, "コード"]
        return a
        # ケースを取得
    def Case(self):
        a = read_lots.loc[self.name, "ケース"]
        return a

    # 最小ロットを取得
    def Lot(self):
        a = read_lots.loc[self.name, "最小ロット"]
        return a

    # 本店の在庫
    def Honten(self):
        a = read_lots.loc[self.name, "本店"]
        return a

    # 秋田店の在庫
    def Akita(self):
        a = read_lots.loc[self.name, "秋田店"]
        return a

    # 由利本荘店の在庫
    def Honjo(self):
        a = read_lots.loc[self.name, "由利本荘店"]
        return a


# sample.csvからデータを取り出す
class sample_c():
    def __init__(self, name):
        self.name = name
# 名前からサンプル名を取得
    def sample_data(self):
        sample = sample_csv.loc[self.name,"サンプル名"]
        return sample



    #sampleの商品名の配列を取得
    def sample_values(self):
        sample_names = sample_csv.index
        return sample_names

# n = order(name="明治ﾌﾟﾛﾋﾞｵﾖｰｸﾞﾙﾄLG21ﾄﾞﾘﾝ",shop="本店")
# print(n.Tnum())
# print(today_csv[today_csv["支店名"] == "本店"])
