class BinNode(object):
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


class BinTree(object):
    def __init__(self):
        self.__root = None

    def is_empty(self):
        return self.__root is None

    def get_root(self):
        return self.__root

    def get_left_node(self):
        return self.__root.left_node

    def get_right_node(self):
        return self.__root.right_node

    def set_root(self, root_node):
        self.__root = root_node

    def set_left_node(self, left_node):
        self.__root.left_node = left_node

    def set_right_node(self, right_node):
        self.__root.right_node = right_node

    def mid_print(self, bin_tree):
        if bin_tree is None:
            return False
        self.mid_print(bin_tree.left_node)
        print(bin_tree.data)
        self.mid_print(bin_tree.right_node)

    def sort_node(self, bin_tree):
        if bin_tree is None:
            return False
        if bin_tree.left_node.data > bin_tree.data:
            bin_tree.left_node.data, bin_tree.data = bin_tree.data, bin_tree.left_node.data
        if bin_tree.right_node.data < bin_tree.data:
            bin_tree.right_node.data, bin_tree.data = bin_tree.data, bin_tree.right_node.data
        self.sort_node(bin_tree.left_node)
        self.sort_node(bin_tree.riht_node)


