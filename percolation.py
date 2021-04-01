from unionfind import WeightedUnionFind


class Percolation:

    def __init__(self, n):
        self.flat_grid_len = n * n
        self.per_row_len = n
        self.topUF = WeightedUnionFind(n + 1)
        self.commonUF = WeightedUnionFind(n + 2)
        self.grid = [[False for _ in range(n)] for _ in range(n)]
        self.open_tile_count = 0
        self.virtual_top = self.flat_grid_len + 1
        self.virtual_bottom = self.flat_grid_len + 2

    def open(self, row, col):
        """
            Open the current coordinate and connect it with surround available blocks
        """
        self.grid[row][col] = True
        self.open_tile_count += 1
        self.connect_to_virtual_point(row, col)
        self.connect_to_surrounds(row, col)

    def close(self, row, col):
        self.grid[row][col] = False
        self.open_tile_count -= 1

    def connect_to_virtual_point(self, row, col):
        """
            Connect to a virtual point 
        :param row:
        :param col:
        :return:
        """
        flattened = self.flatten_coordinate(row, col)
        if row == 0:
            self.connect_to_point(self.virtual_top, flattened)
        if row == self.per_row_len:
            self.commonUF.union(self.virtual_bottom, flattened)

    def connect_to_surrounds(self, row, col):
        if self.is_block_available(row - 1, col):
            self.connect_to_point(self.flatten_coordinate(row - 1, col), self.flatten_coordinate(row, col))
        elif self.is_block_available(row + 1, col):
            self.connect_to_point(self.flatten_coordinate(row + 1, col), self.flatten_coordinate(row, col))
        elif self.is_block_available(row, col - 1):
            self.connect_to_point(self.flatten_coordinate(row, col - 1), self.flatten_coordinate(row, col))
        elif self.is_block_available(row, col + 1):
            self.connect_to_point(self.flatten_coordinate(row, col + 1), self.flatten_coordinate(row, col))

    def connect_to_point(self, a, b):
        self.topUF.union(a, b)
        self.commonUF.union(a, b)

    def is_block_available(self, row, col):
        return self.is_on_grid(row, col) and self.is_open(row, col)

    def is_on_grid(self, row, col):
        return 0 <= row <= self.per_row_len and 0 <= col <= self.per_row_len

    def flatten_coordinate(self, row, col):
        return row * self.per_row_len + col

    def is_open(self, row, col):
        return self.grid[row][col]

    def is_full(self, row, col):
        return self.topUF.find_root(self.virtual_top) == self.topUF.find_root(self.flatten_coordinate(row, col))

    def is_percolated(self):
        return self.topUF.find_root(self.virtual_top) == self.commonUF.find_root(self.virtual_bottom)
