import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import networkx as nx
import matplotlib.pyplot as plt


def create_graph(G, node, pos=None, label=None, x=0, y=0, layer=1):
    """

    :param layer:
    :param y:
    :param x:
    :param pos:
    :param node:
    :type label: object
    """
    if label is None:
        label = {}
    if pos is None:
        pos = {}
    if pos is None:
        pos = {}
    pos[node] = (x, y)
    label[node] = node.val
    if node.left:
        G.add_edge(node, node.left)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node, node.right)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return G, pos, label


def draw(node):  # 以某个节点为根画图
    G = nx.DiGraph()
    G, pos, label = create_graph(G, node)
    fig, ax = plt.subplots(figsize=(5, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(G, pos, ax=ax, labels=label, with_labels=True, node_size=4000)
    plt.show()


def deserialize(inputList: List[int]):
    """

        :type inputList: object
        """
    # n: the index of node
    # m: the num of None before node
    # node.left: (n - m) * 2 + 1
    # node.right: (n - m) * 2 + 2
    if not inputList: return None
    l = len(inputList)
    root, i = TreeNode(inputList[0]), 1
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if i < l and inputList[i]:
            node.left = TreeNode(inputList[i])
            queue.append(node.left)
        i += 1
        if i < l and inputList[i]:
            node.right = TreeNode(inputList[i])
            queue.append(node.right)
        i += 1
    return root


def parseListToChain(list: List) -> ListNode:
    head = ListNode(None)
    temp = head
    for i in list:
        temp.next = ListNode(i)
        temp = temp.next
    return head.next


def print_by_layer_1(root):
    """
    2. 逐行打印——初级版：
    用line/current_line 控制换行，在入队时候即加入行号信息
    """
    print("逐行打印")
    if not root:
        return
    queue = []  #
    current_line = 0
    queue.append([current_line, root])
    while len(queue) > 0:
        line, node = queue.pop(0)
        # 核心判断：是否换行
        if line != current_line:
            print()  # 不同时换行，print()函数默认end=“\n”
            current_line = line
        print(node.val, end=" ")
        if node.left:
            queue.append([line + 1, node.left])  # 将本节点的行号和左子节点入队
        if node.right:
            queue.append([line + 1, node.right])  # 将本节点的行号和右子节点入队
    print()


def print_chain(head: ListNode):
    while head:
        print("{} --> ".format(head.val), end="")
        head = head.next
    print('NULL')
