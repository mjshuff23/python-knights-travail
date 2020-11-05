import tree


class KnightPathFinder:
    def __init__(self, coords):
        self._coords = coords
        self._root = tree.Node(coords)
        self._considered_positions = set(coords)

    def get_valid_moves(self, pos):
        # valid_moves = range(0, 8, 1)
