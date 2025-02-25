class BinarySearch:
    def __init__(self, array: list[int] | None = None):
        self.array = array

    def index_of(self, target: int, array: list[int] | None = None) -> int:
        if array is not None:
            self.array = array

        left, right = 0, len(self.array)

        while left != right:
            mid = left + (right - left) // 2

            if target > self.array[mid]:
                left = mid + 1
            else:
                right = mid

        return left if self.array[left] == target else len(self.array)

        """Alternative implementation
        left, right = 0, len(self.array) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if self.array[mid] == target:
                return mid
            elif target > self.array[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return len(array)
        """

    def lower_bound(self, target: int, array: list[int] | None = None) -> int:
        """Lower bound of target value refers to the smallest index at which it can be inserted without disturbing the array's order."""
        pass

    def upper_bound(self, target: int, array: list[int] | None = None) -> int:
        """Upper bound of target value refers to the largest index at which it can be inserted without disturbing the array's order."""
        pass


def test():
    import random

    array = sorted([random.randint(-1000, 1000) for _ in range(10)])
    print(array)

    binary_search = BinarySearch(array)

    for i in range(10):
        target = random.randint(-1000, 1000)

        print(f"Target value: {target} | index: {binary_search.index_of(target)}")
        print(f"Target value: {array[i]} | index: {binary_search.index_of(array[i])}")


if __name__ == "__main__":
    test()
