from .tree_node import BinaryTreeNode as Node


class BST:
    def __init__(self, root: Node | None = None):
        self._root = root

    def insert(self, key: int):
        #TODO: Not implemented
        return NotImplementedError

    def delete(self, key: int):
        #TODO: Not implemented
        return NotImplementedError

    def search(self, key: int) -> Node:
        return self._search(key, self._root)

    def has_key(self, key: int) -> bool:
        return self._search(key, self._root) is not None

    def traverse_inorder(self) -> list[int]:
        keys: list[int] = []

        def _traverse_inorder(node: Node):
            if node is not None:
                _traverse_inorder(node.left)
                keys.append(node.value)
                _traverse_inorder(node.right)

        _traverse_inorder(self._root)

        return keys

    def traverse_preorder(self) -> list[int]:
        keys: list[int] = []

        def _traverse_preorder(node: Node):
            if node is not None:
                keys.append(node.value)
                _traverse_preorder(node.left)
                _traverse_preorder(node.right)

        _traverse_preorder(self._root)

        return keys

    def traverse_postorder(self) -> list[int]:
        keys: list[int] = []

        def _traverse_postorder(node: Node):
            if node is not None:
                _traverse_postorder(node.left)
                _traverse_postorder(node.right)
                keys.append(node.value)

        _traverse_postorder(self._root)

        return keys

    def minimum(self) -> int | None:
        candidate_node = self._minimum_node(self._root)

        return None if candidate_node is None else candidate_node.value

    def maximum(self) -> int | None:
        candidate_node = self._maximum_node(self._root)

        return None if candidate_node is None else candidate_node.value

    def predecessor(self, key: int) -> int | None:
        """Returns key of next smaller element to given key or None if given key is the smallest."""
        node_with_key = self.search(key)

        if node_with_key is None:
            return None
        elif node_with_key.left is None:
            return node_with_key.value
        else:
            return self._maximum_node(node_with_key.left).value

    def successor(self, key: int) -> int | None:
        """Returns key of next larger element to given key or None if given key is the largest."""
        node_with_key = self.search(key)

        if node_with_key is None:
            return None
        else:
            # To handle duplicate keys, we will first get to the right most node with given key
            while node_with_key.right and (
                node_with_key.value == node_with_key.right.value
            ):
                node_with_key = node_with_key.right

            if node_with_key.right is None:
                return node_with_key.value
            else:
                return self._minimum_node(node_with_key.right).value

    @staticmethod
    def _search(key: int, start_node: Node) -> Node:
        if start_node is None:
            return None

        if key == start_node.value:
            return start_node
        elif key < start_node.value:
            return BST._search(start_node.left)
        else:
            return BST._search(start_node.right)

    @staticmethod
    def _maximum_node(node: Node) -> Node:
        if node is None:
            return None

        if node.right is None:
            return node

        return BST._maximum_node(node.right)

    @staticmethod
    def _minimum_node(node: Node) -> Node:
        if node is None:
            return None

        if node.left is None:
            return node

        return BST._minimum_node(node.left)


def test():
    # TODO: Not all methods have tests
    elements = [4, 10, 1, 234, 2, 15, 1]

    bst = BST()

    assert not bst.search(4)

    for element in elements:
        bst.insert(element)
        assert bst.search(element)

    assert bst.search(2)
    bst.delete(2)
    assert not bst.search(2)

    sorted_elements = bst.traverse_inorder()
    assert sorted_elements == sorted(elements)


if __name__ == "__main__":
    test()
