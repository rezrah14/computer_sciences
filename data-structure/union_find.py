
class DisjointSet:
    """
    Also known as Union-Find data structure
    """

    def __init__(self, n):
        self._id = [i for i in range(n)]
        self._sz = [1 for _ in range(n)]
        self._count = n

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        # weighted union strategy
        if self._sz[i] <= self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        self._count -= 1

    def is_connected(self, p, q):
        return self._root(p) == self._root(q)

    def find(self, p):
        return self._root(p)

    def count(self):
        return self._count

    def _root(self, p):
        while self._id[p] != p:
            self._id[p] = self._id[self._id[p]]     # path compression
            p = self._id[p]
        return p
