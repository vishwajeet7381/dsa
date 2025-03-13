class BinarySearch:
    def __init__(self, array: list[int] | None = None):
        self.array = array

    def index_of(self, target: int, array: list[int] | None = None) -> int:
        if array is not None:
            self.array = array

        left, right = 0, len(self.array) - 1

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
        # TODO: implement the method
        raise NotImplementedError

    def upper_bound(self, target: int, array: list[int] | None = None) -> int:
        """Upper bound of target value refers to the largest index at which it can be inserted without disturbing the array's order."""
        # TODO: implement the method
        raise NotImplementedError


def test():
    import random

    array = sorted([random.randint(-1000, 1000) for _ in range(10)])
    print(array)

    binary_search = BinarySearch(array)

    for i in range(10):
        target = random.randint(-1000, 1000)

        assert (
            binary_search.index_of(target) == array.index(target)
            if target in array
            else binary_search.index_of(target) == len(array)
        )
        assert binary_search.index_of(array[i]) == i + 1


if __name__ == "__main__":
    test()
