package dsa.node;

public class BinaryTreeNodeWithValue<K, V> implements NodeWithValue<K, V> {

    private K key;
    private V value;
    private BinaryTreeNodeWithValue<K, V> leftChild;
    private BinaryTreeNodeWithValue<K, V> rightChild;

    @Override
    public K getKey() {
        return key;
    }

    @Override
    public void setKey(K key) {
        this.key = key;
    }

    @Override
    public V getValue() {
        return value;
    }

    @Override
    public void setValue(V value) {
        this.value = value;
    }

    public BinaryTreeNodeWithValue<K, V> getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(BinaryTreeNodeWithValue<K, V> leftChild) {
        this.leftChild = leftChild;
    }

    public BinaryTreeNodeWithValue<K, V> getRightChild() {
        return rightChild;
    }

    public void setRightChild(BinaryTreeNodeWithValue<K, V> rightChild) {
        this.rightChild = rightChild;
    }
}
