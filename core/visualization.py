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

#字符串的预处理
def tokenize(string, maxlen):
    if len(string) >= maxlen:
        return np.full((1,maxlen), '*')
    lst = [i for i in string]
    while len(lst) < maxlen:
        lst.append(' ')
    arr = np.matrix(lst)
    return arr

#制表符的预处理
def drawBranch(len):
    lst = ['├'] + ['─' for _ in range(len-1)] + ['┐']
    return np.matrix(lst)

#定义直接打印矩阵的函数
def printMatrix(M):
    for x in M:
        print(''.join(x))

#先不直接定义函数，先定义一个可视化树图的类
class TreeVisualizer:
    def __init__(self, root): #构造函数，记录左右节点
        self.val = str(root.val)
        self.left = root.left
        self.right = root.right
        self.depth = root.getDepth() #决定一会画图要留多大的空间
        self.maxl = root.getMaxLen() + 3 #每个节点的宽度
    def graph(self): #x和y表示当前画图的坐标
        #接下来先不直接返回字符串，因为字符图标需要递归嵌套，先把图标保存在矩阵中
        #先把空矩阵准备好
        depth = self.depth
        width = self.maxl
        n = 2**(depth-1) * width
        m = 2*depth - 1
        gr = np.full((m,n), ' ')
        #接下来开始递归填充矩阵
        #大致格式如下：
        '''
        A
        ├───────┐     #这里线的长度为 width * 2**(self.getDepth-1)
        left    right
        '''
        gr[0,0:width] = tokenize(self.val, width)
        #先设置边界条件：如果是树叶节点则停止递归
        if self.left == None and self.right == None:
            return gr
        #接下来是单分支节点：不区分左右子树：
        if (self.left is None) or (self.right is None):
            child = self.left if self.left != None else self.right
            gr[1,0] = '│'
            childgr = TreeVisualizer(child).graph()
            m2, n2 = childgr.shape
            gr[2:2+m2,0:n2] = childgr
            return gr
        #接下来是双分支节点：
        if (self.left is not None) and (self.right is not None):
            len = 2**(depth-2) * width
            gr[1,0:len+1] = drawBranch(len)
            lftgr = TreeVisualizer(self.left).graph()
            rhtgr = TreeVisualizer(self.right).graph()
            ml,nl = lftgr.shape
            mr,nr = rhtgr.shape
            gr[2:2+ml,0:nl] = lftgr
            gr[2:2+mr,len:len+nr] = rhtgr
            return gr


#以下是测试代码
tree = TreeNodeClass.buildTree([4,1,6,2,7,5,'null',8,12,123,1234])
vis = TreeVisualizer(tree)
printMatrix(vis.graph())
        