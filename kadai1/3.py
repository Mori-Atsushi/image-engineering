# -*- coding:utf-8 -*-
# 指定した同じ大きさの2枚の白黒濃淡画像を読み込み、それらを指定した割合で合成し、できた画像を指定した名前で保存する。

import numpy as np
import cv2
import sys

if __name__ == '__main__':
	args = sys.argv #コマンドライン引数を取得
	if len(args) != 5: #コマンドライン引数が3つでなければ	
		print '引数が間違っています'
	else:
		img1 = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
		img2 = cv2.imread(args[2], cv2.IMREAD_UNCHANGED) #読み込み
		x = float(args[3])
		if x > 1 or x < 0:
			print '0~1の値を指定してください'
			sys.exit()
		add = cv2.addWeighted(img1 , x ,img2 , 1.0 - x, 0) #合成
		cv2.imwrite(args[4], add) #書き込み