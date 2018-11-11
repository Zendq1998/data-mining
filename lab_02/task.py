# coding=UTF-8
import apriori1
# 定义最小支持度
minSupport = 0.4
# 收集数据集
dataMap = apriori1.loadDataSet('mushroom.dat')
# 创建候选数据集C1
#C1 = apriori1.createC1(dataMap)
# 计算C1在数据集中的支持度，并返回并返回支持度大于最小支持度（minSupport）的数据
#L1, supportData = apriori1.scanD(dataMap, C1, minSupport)

# 找出数据集中支持度>=0.4的所有的频繁项集
L, supportData =  apriori1.apriori(dataMap, minSupport)

# 从所有的频繁项集中找出频繁3-项集L3
L3 = L[2]

# 遍历频繁3-项集L3，筛选出包含特征值‘2’的频繁3-项集放入结果集中
resultSet = []
for freqSet3 in L3:
  if '2' in freqSet3:
    resultSet.append(freqSet3)

print resultSet

# 置信度规则列表
bigRuleList =  apriori1.generateRules(L, supportData)

# 遍历置信度规则列表，找出毒蘑菇的强关联规则的特征集
for item in bigRuleList:
  if (item[0] == frozenset(['2'])):
    print item



