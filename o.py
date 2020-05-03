import pandas as pd
import numpy as np
import math
from test import products_c, sample_c, order
# 支店名を配列にする
shop = ["本店", "秋田店", "由利本荘店"]
yokote = []
akita = []
honjo = []



# 発注リスト.csvをpandasで取り込む
# today_csv = pd.read_csv("発注リスト.csv", encoding="cp932", header=1, index_col=5)


# 商品の情報を取得
read_lots = pd.read_csv("products.csv", index_col=0)
# 商品名を取得
pr = read_lots.index

# サンプルの情報を取得
sample_csv = pd.read_csv("sample.csv", index_col=0)
# 商品名を取得
sample_names = sample_csv.index

# 商品ごとに処理
for i in pr:
    inst = products_c(i)
    code = inst.Code()
    case = inst.Case()
    lot = inst.Lot()
    # 店舗ごとの在庫の取得
    honten = inst.Honten()
    akita = inst.Akita()
    honjo = inst.Honjo()
    s = {"本店": honten, "秋田店": akita, "由利本荘店": honjo}

    # 店舗ごとに処理
    for n in shop:
        # 商品名と店舗名を入れてインスタンス化
        instan = order(name=i,shop=n)
        # 配達数
        num = instan.Tnum()
        # サンプル商品がある場合の処理
        if i in sample_names:
            sample = sample_c(i)
            sample_name = sample.sample_data()
            sa = order(name=sample_name,shop=n)
            if sa:
                sample_num = sa.Tnum()
                num += sample_num
        total = num
        # 店舗の在庫
        now = s[n]

        # お届け数が在庫よりも多い場合は発注
        if total >= now:
            # お届け総数から在庫数を引く
            order_num = total - now
            # ロットで最低限必要な数を計算
            hachu = math.ceil(order_num / lot)
            # 発注する本数を計算
            hachu_num = hachu * lot
            # 発注する本数からケース分を計算
            hachu_case = math.floor(hachu_num / case)
            hachu_lot = hachu_num % case
            # 在庫を計算
            zaiko = hachu_num - order_num



            with open(n + "本日の発注.txt", mode="a") as f:
                f.write("商品名：{}({})\n".format(i, code))
                f.write("発注ケース：{}\n".format(hachu_case))
                f.write("発注ロット：{}\n".format(hachu_lot))
                f.write("お届け総数：{}\n".format(total))
                f.write("今回在庫：{}\n\n".format(zaiko))

        # 在庫数が多くあるときの設定
        else:
            zaiko = now - total

            with open(n + "本日の発注.txt",mode="a") as f:

                f.write("商品名：{}({})\n".format(i, code))
                f.write("お届け総数：{}\n".format(total))
                f.write("発注：なし\n")
                f.write("今回在庫：{}\n\n".format(zaiko))

    print("\n")
