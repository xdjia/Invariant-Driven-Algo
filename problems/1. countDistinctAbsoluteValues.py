# Problem: Given a sorted list of integers, count the number of different absolute values.

def countDistinctAbsoluteValues(nums: list[int]) -> int:
    """
    Counts the number of distinct absolute values in a sorted list of integers.

    Parameters:
    nums (List[int]): A sorted list of integers (can include negatives).

    Returns:
    int: The count of distinct absolute values.
    """

    left, right = 0, len(nums) - 1
    count = 0
    last_seen = None

    # Invariant check: count should match the reference function's output for the excluded middle part.
    assert count == ref(nums[:left] + nums[right + 1:]), "Invariant failed!"
    while left <= right:

        # Absolute values at both ends of the current window.
        left_abs = abs(nums[left])
        right_abs = abs(nums[right])

        # Choose the larger absolute value to process and move the respective pointer.
        if left_abs > right_abs:
            current = left_abs
            left += 1
        else:
            current = right_abs
            right -= 1

        # Invariant check: current should be the minimum absolute value in the current window.
        assert current == min(
            abs(n) for n in nums[:left] + nums[right + 1:]), "Invariant failed!"

        # Only count if the current absolute value is different from the last seen.
        if current != last_seen:
            count += 1
            last_seen = current

        # Invariant check: count should match the reference function's output for the excluded middle part.
        assert count == ref(
            nums[:left] + nums[right + 1:]), "Invariant failed!"

    # Final invariant check: count should equal the reference function's result.
    #   Actually, this must hold because `left > right`, so `nums[:left] + nums[right + 1:] == nums`
    assert count == ref(nums), "Final invariant failed!"

    return count


def ref(nums: list[int]) -> int:
    """
    Reference function using a set to count distinct absolute values.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    int: The count of distinct absolute values.
    """
    return len(set(abs(n) for n in nums))


# Example Usage:
test_cases = [
    [-4, -2, 0, 1, 3, 5],    # Mixed values with distinct absolute values
    [-3, -1, 0, 0, 2, 3],    # Repeated absolute values
    [],                      # Empty list
    [-5, -5, -5, -5],        # All negative, same absolute value
    [0, 0, 0],               # Only zeros
]

# Testing the function with example cases
for case in test_cases:
    result = countDistinctAbsoluteValues(case)
