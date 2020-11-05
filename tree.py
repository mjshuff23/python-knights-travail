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
        if self._parent:
            print(self._parent)
            self.parent.remove_child(self)
        self._parent = node
        node.add_child(self)

    def add_child(self, node):
        print('pre-count', self._children.count(node))
        if self._children.count(node) == 0:
            print('postcount', self._children.count(node))
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        try:
            print('pre-removal', self._children)
            self._children.remove(node)
            node.parent = None
        except:
            print('Node does not exist')


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
# node3.parent = node2
# node1.add_child(node3)
# node1.add_child(node3)

print(node1.children)
print(node2.children)
