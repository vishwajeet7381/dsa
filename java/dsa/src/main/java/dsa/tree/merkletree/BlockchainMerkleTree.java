package dsa.tree.merkletree;

import java.util.List;

import dsa.node.BinaryTreeNodeWithValue;

public class BlockchainMerkleTree<K, V> implements MerkleTree<K, V> {
    
    private BinaryTreeNodeWithValue<K, V> rootNode;

    @Override
    public BinaryTreeNodeWithValue<K, V> buildMerkleTree(List<K> dataList) {
        return rootNode;
    }
}
