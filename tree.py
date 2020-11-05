class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    # def __repr__(self):
    #     print(
    #         f'Node val: {self.value}, par: {self.parent}'
    #     )

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if not node:
            self._parent = None
            return
        if self._parent != node:
            if self._parent != None:
                self.parent.remove_child(self)
        self._parent = node
        node.add_child(self)

    def add_child(self, node):
        if self._children.count(node) == 0:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        try:
            self._children.remove(node)
            node.parent = None
        except:
            print('Node does not exist')

    def breadth_first_search(self, value):
        queue = [self]
        while len(queue) > 0:
            node = queue.pop()
            if node.value == value:
                return True
            else:
                queue.extend(node.children)
        return False


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2
# node1.add_child(node3)
# node1.add_child(node3)

# print(node1.children)
# print(node2.children)
