# Problem Information

Link: [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

# Understanding

- **Input:** integer array
- **Output:** return `true` if any value appears at least twice (duplicate exists), else `false` (all elements are distinct)

# Approach(es)

## Approach 1: Naive Iteration

### Logic

1. For each element in array, check if any element to its left is the same
2. Return `true` at first instance of finding a duplicate
3. Return `false` at the end if no duplicates found

### Analysis

- **Time Complexity:**
  - **Worst case:** $O(n^2)$, where n = length(input_array)
- **Auxiliary Space:** $O(1)$
- **Implementation:** [Python, got TLE](https://leetcode.com/problems/contains-duplicate/submissions/1494393498)

## Approach 2: Sorting

### Logic

1. Sort the array in non-decreasing/non-increasing order using one of worst case $O(n \times \log n)$ algorithm (e.g. merge sort, heap sort)
2. If duplicates exist it will be adjacent in the sorted array
3. Iterate and compare each element to its next element:
   - If equal, return `true`
4. Return `false` at the end

### Analysis

- **Time Complexity:**
  - **Worst case:** $O(n \times \log n)$
- **Auxiliary Space:** Depends on choice of sorting algorithm used, in-place algorithm (e.g. heap sort) uses $O(1)$, merge sort uses $O(n)$
- **Implementation:** [Python](https://leetcode.com/problems/contains-duplicate/submissions/1494496931)

## Approach 3: Hash Table

### Logic

1. Create an empty hash table
2. For each element in array:
   - Check if element exists in hash table
   - If exists, return `true`
   - If not, store element in hash table
3. Return `false` at the end

### Analysis

- **Time Complexity:**
  - **Average case:** $O(n)$, where n = length(input_array)
- **Auxiliary Space:** $O(n)$
- **Implementation:** [Python](https://leetcode.com/problems/contains-duplicate/submissions/1303820200/)

## Approach 4: Balanced Binary Search Tree

### Logic

1. Create an empty balanced binary search tree
2. For each element in array:
   - Check if element exists in tree
   - If exists, return `true`
   - If not, store element in tree
3. Return `false` at the end

### Analysis

- **Time Complexity:**
  - **Worst case:** $O(n \times \log n)$, where n = length(input_array)
- **Auxiliary Space:** $O(n)$
- **Implementation:** Not implemented

# Notes

- The problem requires efficient data structures that support `insert`, `delete`, and `membership` operations
- Hash table provides the best average-case time complexity of $O(n)$
- Python's `set` is implemented using `hash table`
- While balanced BST solution is theoretically possible, it's less efficient than hash table approach
- The naive solution, while using minimal space, is too slow for large inputs (results in Time Limit Exceeded)
- Sorting approach offers a good balance of time complexity and space efficiency when used with in-place sorting algorithms