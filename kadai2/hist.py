# -*- coding:utf-8 -*-
# ファイル名を指定して画像の分散とヒストグラムを求める

import pylab as plt
import numpy as np

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