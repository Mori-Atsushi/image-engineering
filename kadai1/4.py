# -*- coding:utf-8 -*-
# 指定した白黒濃淡画像を読み込み、その画像の各画素の値を指定しただけ変化させて、指定した名前で保存する。

import numpy as np
import cv2
import sys

if __name__ == '__main__':
	args = sys.argv #コマンドライン引数を取得
	if len(args) != 4: #コマンドライン引数が3つでなければ	
		print '引数が間違っています'
	else:
		img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
		x = int(args[2])
		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				if img[i][j] + x > 255: #255を超える場合
					img[i][j] = 255
				elif img[i][j] + x < 0: #0を下回る場合
					img[i][j] = 0
				else:
					img[i][j] += x #加算
		cv2.imwrite(args[3], img) #書き込み