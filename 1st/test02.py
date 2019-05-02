# -*- coding: UTF-8 -*-
import numpy as np
import operator

from knn import classify0
from file2matrix import file2matrix
from autoNorm import autoNorm

def classifyPerson():
  resultList = ['讨厌', '有些喜欢', '非常喜欢']

  #三维特征用户输入
  precentTats = float(input("玩视频游戏所耗时间百分比:"))
  ffMiles = float(input("每年获得的飞行常客里程数:"))
  iceCream = float(input("每周消费的冰激淋公升数:"))

  filename = "datingTestSet.txt"

  datingDataMat, datingLabels = file2matrix(filename)
  normMat, ranges, minVals = autoNorm(datingDataMat)

  #生成NumPy数组,测试集
  inArr = np.array([ffMiles, precentTats, iceCream])
  #测试集归一化
  norminArr = (inArr - minVals) / ranges
  #返回分类结果
  classifierResult = classify0(norminArr, normMat, datingLabels, 3)
  #打印结果
  print("你可能%s这个人" % (resultList[classifierResult-1]))


if __name__ == '__main__':
    classifyPerson()