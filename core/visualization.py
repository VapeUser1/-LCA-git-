#本模块用于实现二叉树的可视化
#不同层的节点纵向排列，每一层的节点横向排列
#形式如下：
'''
A
├───────┐
B       C
├───┐   ├───┐
D   E   F   G   
'''
import TreeNodeClass
import numpy as np

char_1 = '├'
char_2 = '─'
char_3 = '┐'
char_4 = '│'

#先不直接定义函数，先定义一个可视化树图的类
class TreeVisualizer:
    def __init__(self, root): #构造函数，记录左右节点
        self.val = str(root.val)
        self.left = root.left
        self.right = root.right
        self.depth = root.getDepth() #决定一会画图要留多大的空间
        #self.width_0 = root.getMaxLen() + 3 #每个节点的宽度
    def graph(self, root, x, y): #x和y表示当前画图的坐标
        #接下来先不直接返回字符串，因为字符图标需要递归嵌套，先把图标保存在矩阵中
        #先把空矩阵准备好
        depth = root.getDepth()
        width = root.getMaxLen() + 3
        n = 2**(depth-1) * width
        m = 2*depth - 1
        gr = np.full((m,n), ' ', dtype='S')
        return gr

#以下是测试代码
tree = TreeNodeClass.buildTree([1,2,3,4,5,6,7])
vis = TreeVisualizer(tree)
print(vis.graph(tree,1,1))

        