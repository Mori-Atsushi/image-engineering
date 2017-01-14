# -*- coding:utf-8 -*-
# ファイル名を指定して画像の分散とヒストグラムを求める

import pylab as plt
import numpy as np
import cv2
import sys

class Hist:
    def __init__(self, img):
        self.__arr = np.array([])
        for data in img:
            self.__arr = np.append(self.__arr, np.array(data), axis=0)

    #分散の取得
    def getVar(self):
        var = np.var(self.__arr) #分散の計算
        return var

    #ヒストグラムの表示
    def showHist(self, bins):
        plt.hist(self.__arr, bins=bins, facecolor='black')
        plt.title("Histgram")
        plt.show()

if __name__ == '__main__':
    args = sys.argv #コマンドライン引数を取得
    if len(args) != 2: #コマンドライン引数が3つでなければ	
        print '引数が間違っています'
    else:
        img = cv2.imread(args[1], cv2.IMREAD_UNCHANGED) #読み込み
        hist = Hist(img)
        print hist.getVar()
        hist.showHist(1000)