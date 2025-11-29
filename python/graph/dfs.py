class DFS:
    """Depth First Search (DFS) is a graph traversal technique.
    """
    def __init__(self, graph: list[list[int]]):
        self._graph: list[list[int]] = graph
        self._num_vertices: int = len(self._graph)

    def search(self, target: int, source: int) -> bool:
        raise NotImplementedError