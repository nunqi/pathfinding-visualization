class Node:
    def __init__(self, v, p=None):
        self.value = v
        self.parent = p
        self.children = []

    def find(self, x):
        if self.value == x: return self
        for node in self.children:
            n = node.find(x)
            if n: return n
        return None


class Tree:
    def __init__(self, r):
        self.root = Node(r)

    def add(self, v, p):
        self._add_aux(self.root, v, p)

    def _add_aux(self, n, v, p):
        if n.value == p:
            n.children.append(Node(v, n))
        for i in n.children:
            self._add_aux(i, v, p)

    def show(self):
        self.show_aux(self.root)
     
    def show_aux(self, r):
        print(r.value)
        for i in r.children:
            self.show_aux(i)

    def distance(self, v):
        count = 0
        current = self.root.find(v)

        while current.parent:
            count += 1
            current = current.parent

        return count
    
    def path(self, v):
        path = []
        current = self.root.find(v)

        while current.parent:
            path.append(current.value)
            current = current.parent

        return path

    def get_all_edges(self):
        return self.get_all_edges_aux(self.root, [])

    def get_all_edges_aux(self, r, l):
        for i in r.children:
            l.append([r.value, i.value])
            self.get_all_edges_aux(i, l)
        return l
