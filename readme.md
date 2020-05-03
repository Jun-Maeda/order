# 発注リスト.csvから店舗ごとの発注数を計算して出力する
必要な商品数をCSVから読み込み、商品ごとに現在の在庫数などの情報をproducts.csvから読み込んで
今回発注するのに必要な数やケース、ロット数を計算して
店舗ごとにテキストファイルに出力します。


# Features
products.csvを追加、変更することで商品が追加変更されても対応がすぐにできます。
また、sample.csvで商品情報を入力すると、サンプル商品など、products.csvに登録の名前と違う場合も、登録されているものと数を合わせることができる。
# Requirement
* pandas
* numpy
* math
# Installation
```
pip install pandas
pip install numpy
```
# Usage
```
git clone https://github.com/Jun-Maeda/order.git
cd order
python o.py
```

# Author
* 作成者 jun maeda
