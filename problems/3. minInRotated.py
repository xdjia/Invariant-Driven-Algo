# Problem: Find the minimum in a rotated and sorted array.

def minInRotated(nums: list[int]) -> int | None:
    """
    Finds the minimum element in a rotated sorted array using binary search.

    Parameters:
    nums (List[int]): A rotated sorted array of integers.

    Returns:
    int: The minimum element in the array.
    """
    # Edge case: If the list is empty, return None.
    if not nums:
        return None

    l, r = 0, len(nums) - 1

    # Invariant: 0 <= l <= ref(nums)[1] <= r <= len(nums) - 1
    assert 0 <= l <= ref(nums)[1] <= r <= len(nums) - 1
    while l < r:
        m = (l + r) // 2

        # If the middle element is greater than the last element, search the right half.
        if nums[m] > nums[-1]:
            l = m + 1
        else:
            r = m

        # Invariant check
        assert 0 <= l <= ref(nums)[1] <= r <= len(nums) - 1

    # Final invariant check: The index `l` should correspond to the minimum element.
    #   This is a corollary from the loop invariant.
    assert l == ref(nums)[1]

    return nums[l]


def ref(nums: list[int]) -> tuple[int, int]:
    """
    Reference function to find the minimum value and its index using Python's built-in functions.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: The minimum value and its index.
    """
    return min(nums), nums.index(min(nums))


# Example Usage:
test_cases = [
    [3, 4, 5, 1, 2],       # Example 1: Rotated array with a clear minimum
    [4, 5, 6, 7, 0, 1, 2],  # Example 2: Larger rotated array
    [11, 13, 15, 17],      # Example 3: No rotation (already sorted)
    [1],                   # Edge case: Single element
    [],                    # Edge case: Empty list
]

for nums in test_cases:
    minInRotated(nums)
