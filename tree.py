class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

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
            return
        self._parent = node
        node.add_child = self

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


newNode = Node('hey')
newNode2 = Node('ho')
print(newNode.value)
newNode.add_child(newNode2)
print(newNode.children)
newNode.add_child(newNode2)
print(newNode.children)
