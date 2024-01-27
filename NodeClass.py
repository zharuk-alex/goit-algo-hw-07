import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

    def insert(self, key):
        if key < self.val:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

    def search(self, key):
        if self.val == key:
            return self
        if key < self.val and self.left is not None:
            return self.left.search(key)
        if key > self.val and self.right is not None:
            return self.right.search(key)
        return None

    def min_value_node(self):
        current = self
        while current.left:
            current = current.left
        return current.val

    def max_value_node(self):
        current = self
        while current.right:
            current = current.right
        return current.val

    def sum_values(self):
        total = self.val
        if self.left:
            total += self.left.sum_values()
        if self.right:
            total += self.right.sum_values()
        return total

    def delete(self, key):
        if key < self.val:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.val:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                temp = self.right.min_value_node()
                self.val = temp.val
                self.right = self.right.delete(temp.val)
        return self

    def _add_nodes_edges(self, G, pos, x=0, y=0, level=1):
        G.add_node(self.val)
        pos[self.val] = (x, y)
        if self.left:
            G.add_edge(self.val, self.left.val)
            l = x - 1 / 2**level
            self.left._add_nodes_edges(G, pos, x=l, y=y - 1, level=level + 1)
        if self.right:
            G.add_edge(self.val, self.right.val)
            r = x + 1 / 2**level
            self.right._add_nodes_edges(G, pos, x=r, y=y - 1, level=level + 1)

    def draw_tree(self):
        G = nx.DiGraph()
        pos = {}
        self._add_nodes_edges(G, pos)
        nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000)
        plt.show()


if __name__ == "__main__":
    root = Node(5)

    nodes = [3, 2, 4, 7, 6, 8]

    for n in nodes:
        root.insert(n)

    root.draw_tree()
