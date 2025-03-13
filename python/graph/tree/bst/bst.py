from ..tree_node import BinaryTreeNode as Node


class BST:
    def __init__(self, root: Node | None = None):
        self._root = root

    def insert(self, key: int):
        return NotImplementedError

    def delete(self, key: int):
        return NotImplementedError

    def search(self, key: int) -> bool:
        return NotImplementedError

    def traverse_inorder(self) -> list[int]:
        keys: list[int] = []

        def _traverse_inorder(node: Node):
            if node is None:
                return

            _traverse_inorder(node.left)
            keys.append(node.value)
            _traverse_inorder(node.right)

        _traverse_inorder(self._root)

        return keys

    def traverse_preorder(self) -> list[int]:
        return NotImplementedError

    def traverse_postorder(self) -> list[int]:
        return NotImplementedError


def test():
    return NotImplementedError


if __name__ == "__main__":
    test()
