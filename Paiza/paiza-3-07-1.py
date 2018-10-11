# coding: utf-8
'''
演習課題「西暦年と昭和年の対応表を作ろう」
西暦年と昭和年の対応表を作成してください。対応表は、「西暦XXXX年は昭和YY年です」と表示します。なお、昭和年は、西暦1926年から西暦1988年までの期間で、「西暦年 - 1925」で求めることができます。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
西暦1926年は昭和1年です
西暦1927年は昭和2年です
西暦1928年は昭和3年です
...
西暦1988年は昭和63年です
'''

# 西暦年と昭和年の対応表
# 1926年から1988年までをループで出力
# ループ内で、各西暦年を昭和年に変換
for seireki in range(1926,1989):
	print(“西暦” + str(seireki) + “年は”, end = “”)
	showa = seireki - 1925
	print(“昭和” + str(showa) + “年です”
