# coding=UTF-8
import trees
import treePlotter
fr = open('lenses.txt')
dataset = []
#labels '年龄', '处方', '散光', '眼镜材质'
labels = ['age', 'prescript', 'astigmatic', 'tearRate']
for line in fr.readlines():
    d = line.strip().split('\t')
    dataset.append(d)
fr.close()

print dataset
print '\n'

print '数据集类的香农熵：'
print  trees.calcShannonEnt(dataset)
print '\n'

bestFeatureColumn = trees.chooseBestFeatureToSplit(dataset)
print '数据集最佳分类的属性是：'
print labels[bestFeatureColumn]
print '\n'

print '决策树：'
Tree = trees.createTree(dataset, labels)
print Tree
firstFeature = Tree.keys()[0]
print firstFeature
firstFeatureValues = Tree[firstFeature].keys()
print firstFeatureValues
print '\n'

treePlotter.createPlot(Tree)

testVec = ['pre', 'myope', 'yes', 'normal']
print '测试数据'
print testVec
labels.append('tearRate')
print '匹配过程：'
result = trees.classify(Tree, labels, testVec)
print '匹配结果：'
print result
print '\n'

# 把树存在磁盘中
print '将树存放磁盘...'
trees.storeTree(Tree, 'myTree.txt')
print '\n'

# 从磁盘中取出树
print '再从磁盘中读取树：'
print trees.grabTree('myTree.txt')


