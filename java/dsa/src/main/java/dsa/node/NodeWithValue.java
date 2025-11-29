package dsa.node;

public interface NodeWithValue<K, V> {
    
    K getKey();

    void setKey(K key);

    V getValue();

    void setValue(V value);
}
