# -*- coding:utf-8 -*-
# DCT変換関係

import numpy as np
import cv2
import sys

#画像をブロッサイズで分割
def imgSplit(img, size):
    dataList = []
    for i in range(0, len(img), size):
        temp = []
        for j in range(0, len(img[i]), size):
            xStart = i
            xEnd = i + size
            yStart = j
            yEnd = j + size
            data = img[xStart:xEnd, yStart:yEnd]
            temp.append(data)
        dataList.append(temp)
    return dataList

#画像を結合する
def imgCombine(data):
    dataList = []
    for d in data:
        temp = np.concatenate(d, axis=1)
        dataList.append(temp)
    img = np.concatenate(dataList, axis=0)
    return img

#DCT変換
def dct(src, flags = 0):
    dataList = []
    for x in src:
        temp = []
        for y in x:
            data = cv2.dct(y, flags = flags)
            temp.append(data)
        dataList.append(temp)
    return dataList

if __name__ == '__main__':
    args = sys.argv #コマンドライン引数を取得
    if len(args) != 2: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        SIZE = 8 #ブロックサイズ
        
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        img = np.float32(img) / 255.0
        data = imgSplit(img, SIZE) #分割
        data = dct(data) #DCT変換
        data = dct(data, flags = cv2.DCT_INVERSE) #DCT逆変換
        img = imgCombine(data) #結合
        img = np.uint8(img * 255.0)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()