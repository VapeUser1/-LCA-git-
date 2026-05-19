#先定义二叉树的类
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)
    def getNodeList(self): #前序排列法列表
        if self.left == None and self.right == None:
            return [self]
        return [self] + self.left.getNodeList() + self.right.getNodeList()
    def getNode(self, val):
        for n in self.getNodeList():
            if n.val == val:
                return n
        return None

#统计节点数
def countNode(root):
    if root == None:
        return 0
    if root.left == 0 and root.right == 0:
        return 1
    return 1 + countNode(root.left) + countNode(root.right)

#通过标准表达式构建树
#需要输入这样的列表：[4,1,6,2,7,5,null,8,...]
#列表中的元素除null外无重复
def buildTree(tree_lst):
    if tree_lst == []:
        return None
    root = TreeNode(tree_lst[0])
    pointer_1 = 1 #表示当前正在添加的子节点
    pointer_2 = 0 #表示当前正在处理的父节点
    node_lst = [root]
    while pointer_1 < len(tree_lst):
        #把新节点连接到树上并添加新节点
        #null节点暂时连上暂时要特殊处理
        if node_lst[pointer_2].left == None and node_lst[pointer_2].val != 'null':
            node_lst.append(TreeNode(tree_lst[pointer_1]))
            node_lst[pointer_2].left = node_lst[-1]
            pointer_1 += 1
            continue
        elif node_lst[pointer_2].right == None and node_lst[pointer_2].val != 'null':
            node_lst.append(TreeNode(tree_lst[pointer_1]))
            node_lst[pointer_2].right = node_lst[-1]
            pointer_1 += 1
            continue
        else:
            pointer_2 += 1 #开始连接下一个节点
    #开始清空所有null节点
    for node in node_lst:
        if node == None:
            continue
        if node.left != None and node.left.val == 'null':
            node.left = None
        if node.right != None and node.right.val == 'null':
            node.right = None
    return root

#判断是否是二叉搜索树
def isBST(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    if root.left == None:
        B = root.val < root.right.val
    elif root.right == None:
        B = root.left.val < root.val
    else:
        B = root.left.val < root.val < root.right.val
    return isBST(root.left) and isBST(root.right) and B

#root = buildTree([1,3,6,4,5,7,8,'null'])
#node2 = root.getNode(3)
#print(node2.right)
#tese