# -*- coding:utf-8 -*-
# ファイル名を指定して画像の分散とヒストグラムを求める

import pylab as plt
import numpy as np
import cv2
import sys

if __name__ == '__main__':
    args = sys.argv #コマンドライン引数を取得
    if len(args) != 2: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        arr = np.array([])
        for data in img:
            arr = np.append(arr, np.array(data), axis=0)

        var = np.var(arr) #分散の計算
        print var

        plt.hist(arr, bins=1000, facecolor='black')
        plt.title("Histgram")
        plt.show()