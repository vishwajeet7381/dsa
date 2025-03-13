from typing import Any


class NAryTreeNode:
    def __init__(self, value: Any = None, parent: "NAryTreeNode" | None = None):
        self.value = value
        self.parent = parent


class BinaryTreeNode(NAryTreeNode):
    def __init__(
        self,
        value: Any = None,
        parent: "BinaryTreeNode" | None = None,
        left: "BinaryTreeNode" | None = None,
        right: "BinaryTreeNode" | None = None,
    ):
        super().__init__(value, parent)
        self.left = left
        self.right = right
