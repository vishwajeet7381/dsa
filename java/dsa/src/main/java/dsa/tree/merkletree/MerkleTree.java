package dsa.tree.merkletree;

import java.util.List;

import dsa.node.BinaryTreeNodeWithValue;

public interface MerkleTree<K, V> {

    BinaryTreeNodeWithValue<K, V> buildMerkleTree(List<K> dataList);
}
