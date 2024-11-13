def trap(height: list[int]) -> int:
    """
    Calculates the total amount of trapped rainwater using a two-pointer approach.

    Parameters:
    height (List[int]): A list of non-negative integers representing the elevation map.

    Returns:
    int: The total amount of trapped water.
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    total_water = 0

    # Two-pointer approach to calculate trapped water.
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            contribute = max(0, left_max - height[left])
            total_water += contribute

            # Invariant: The contribution at index `left` matches the reference function.
            assert contribute == ref(height)[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            contribute = max(0, right_max - height[right])
            total_water += contribute

            # Invariant: The contribution at index `right` matches the reference function.
            assert contribute == ref(height)[right]

        # Invariant: The accumulated total water matches the sum of reference contributions.
        assert total_water == (
            sum(ref(height)[:left + 1]) + sum(ref(height)[right:]))

    # Since left == right, from the loop invariant we directly have:
    assert total_water == sum(ref(height))

    return total_water


def ref(height: list[int]) -> list[int]:
    """
    Reference function that computes the contribution of trapped water at each index
    using precomputed left and right maximum heights.

    Parameters:
    height (List[int]): A list of non-negative integers representing the elevation map.

    Returns:
    List[int]: A list of contributions of trapped water at each index.
    """
    n = len(height)
    if n == 0:
        return []

    left_max = [0] * n
    right_max = [0] * n
    contribute = [0] * n

    # Precompute the maximum heights from the left and right.
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Calculate the trapped water contribution at each index.
    for i in range(n):
        contribute[i] = max(0, min(left_max[i], right_max[i]) - height[i])

    return contribute


# Example Usage:
test_cases = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),  # Example 1
    ([4, 2, 0, 3, 2, 5], 9),                   # Example 2
    ([1, 2, 3, 4, 5], 0),                     # No trapped water
    ([5, 4, 1, 2], 1),                        # Small trapped water
    ([0, 0, 0, 0], 0),                        # All zeros
    ([], 0),                                  # Empty list
]

for height, expected in test_cases:
    result = trap(height)
