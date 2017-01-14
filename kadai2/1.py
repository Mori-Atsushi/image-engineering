# -*- coding:utf-8 -*-
# ファイル名を指定して画像の分散とヒストグラムを求める

import numpy as np
import cv2
import sys

if __name__ == '__main__':
    args = sys.argv #コマンドライン引数を取得
    if len(args) != 2: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        npdata = np.array(img)
        var = np.var(npdata) #分散の計算
        print var