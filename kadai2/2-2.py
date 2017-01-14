# -*- coding:utf-8 -*-
# ファイル名を指定して画像の分散とヒストグラムを求める

import numpy as np
import cv2
import sys
import hist

if __name__ == '__main__':
    args = sys.argv #コマンドライン引数を取得
    if len(args) != 2: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        arr = np.zeros((len(img), len(img[0])), int)

        for j in range(1, len(arr)):
            for i in range(1, len(arr[j])):
                arr[j][i] = int(img[j][i]) - (int(img[j][i - 1]) + int(img[j - 1][i])) / 2 

        hist = hist.Hist(arr)
        print hist.getVar()
        hist.showHist(1000)