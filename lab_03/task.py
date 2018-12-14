# coding=UTF-8
import kMeans
from numpy import *

# 从文本中构建矩阵
dataMat = mat(kMeans.loadDataSet('testSet.txt'))

kMeans.distEclud(dataMat[0], dataMat[1])

# 创建4个质心的聚类算法


c1, c2 = kMeans.kMeans(dataMat, 4)

print '四个质心的坐标：', c1

print '每个点属于哪个类以及与质心的欧式距离', c2

