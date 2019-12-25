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

