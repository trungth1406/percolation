class WeightedUnionFind:

    def __init__(self, n):
        self.idx = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.count = n

    def components_count(self):
        return self.count

    def find_root(self, point):
        self.validate_coordinate(point)
        while point != self.idx[point]:
            point = self.idx[point]
        return point

    def union(self, a, b):
        self.validate_coordinate(a)
        self.validate_coordinate(b)
        a_root = self.find_root(a)
        b_root = self.find_root(b)
        if self.size[a_root] < self.size[b_root]:
            self.idx[a_root] = b_root
            self.size[b_root] += self.size[a_root]
        else:
            self.idx[b_root] = a_root
            self.size[a_root] += self.size[b_root]
        self.count -= 1

    def validate_coordinate(self, p):
        if 0 < p < len(self.idx):
            raise ValueError(f"Input coordinate must in range :0 to {len(self.idx)}")
