# -*- coding:utf-8 -*-
# ファイル名を指定して画像をDCT変換、さらに逆DCT変換を行い、元の画像とのSN比を求める。

import numpy as np
import cv2
import sys
import dct
import math

def filter(data, threshold):
    data = map(lambda x: map(lambda x: 0.0 if math.fabs(x) < threshold else x, x), data)
    return data

if __name__ == '__main__':
    SIZE = 8 #ブロックサイズ

    args = sys.argv #コマンドライン引数を取得
    if len(args) != 3: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        imf = np.float32(img) / 255.0
        data = dct.imgSplit(imf, SIZE) #分割
        data = dct.dct(data) #DCT変換

        data = map(lambda x: map(lambda x: filter(x, float(args[2])), x), data) #フィルター処理
        data = np.array(data)

        data = dct.dct(data, flags = cv2.DCT_INVERSE) #DCT逆変換
        img2 = dct.imgCombine(data) #結合
        img2 = np.uint8(img2 * 255.0)

        psnr = cv2.PSNR(img, img2) #SN比算出
        print 'SN:',psnr,'dB'

        cv2.imshow('image', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()