# -*- coding:utf-8 -*-
# ファイル名を指定してカラー画像を読み込み、指定された2つの色成分を交換した新たなカラー画像を作成し、指定した名前で保存する。

import numpy as np
import cv2
import sys

#bgrのを0~2の数値に直す
def change_bgr(c):
	if c == 'b':
		return 0
	elif c == 'g':
		return 1
	elif c == 'r':
		return 2
	return -1

if __name__ == '__main__':
	args = sys.argv #コマンドライン引数を取得
	if len(args) != 5: #コマンドライン引数が3つでなければ	
		print '引数が間違っています'
	else:
		bgr = [change_bgr(args[2]), change_bgr(args[3])]
		for c in bgr:
			if c == -1:
				print "色成分は「b g r 」のいずれかの文字で指定してください"
				sys.exit()

		img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
		img_bgr = cv2.split(img) #RGB分離
		img_bgr[bgr[0]], img_bgr[bgr[1]] = img_bgr[bgr[1]], img_bgr[bgr[0]] #入れ替え
		img = cv2.merge((img_bgr[0], img_bgr[1], img_bgr[2])) #結合
		cv2.imwrite(args[4], img) #書き込み