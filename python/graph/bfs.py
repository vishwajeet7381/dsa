from collections import deque


class BFS:
    def __init__(self, graph: list[list[int]]):
        self._graph: list[list[int]] = graph
        self._num_vertics: int = len(self._graph)
        self._queue: deque[int] = deque()
        self._discovered: list[bool] = [False] * self._num_vertics

    def search(self, source: int = 0):
        self._queue.append(source)
        self._discovered[source] = True

        num_discovered = 1

        while (num_discovered == self._num_vertics) or (len(self._queue) > 0):
            vertex1 = self._queue.popleft()

            for vertex2 in self._graph[vertex1]:
                if not self._discovered[vertex2]:
                    self._queue.append(vertex2)
                    self._discovered[vertex2] = True
                    num_discovered += 1

    def get_discovered(self):
        return self._discovered


def main():
    # Graph represented using collection of adjacency list
    graph = [[1, 2, 3], [0], [0, 3], [0, 2], [5], [4]]

    bfs = BFS(graph)

    bfs.search()

    discovered = bfs.get_discovered()

    for vertex, discovery in enumerate(discovered):
        print(vertex, discovery, sep=" ")


if __name__ == "__main__":
    main()
