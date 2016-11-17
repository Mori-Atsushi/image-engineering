# -*- coding:utf-8 -*-
# ファイル名を指定して白黒濃淡動画を読み込み、画面に表示し、指定した名前で保存する。

import numpy as np
import cv2
import sys

if __name__ == '__main__':
	args = sys.argv #コマンドライン引数を取得
	print args
	if len(args) != 3: #コマンドライン引数が3つでなければ	
		print '引数が間違っています'
	else:
		img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED)
		cv2.imshow(args[1], img) #表示
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.imwrite(args[2], img) #書き込み