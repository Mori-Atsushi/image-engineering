# -*- coding:utf-8 -*-
# ファイル名を指定して画像の分散とヒストグラムを求める

import cv2
import sys
import hist

if __name__ == '__main__':
    args = sys.argv #コマンドライン引数を取得
    if len(args) != 2: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        hist = hist.Hist(img)
        print hist.getVar()
        hist.showHist(1000)