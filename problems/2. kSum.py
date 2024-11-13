# Problem: Given an integer `target`, a number `k>=2`, and a list of integers, find all k-tuples that sum up to `target`.

from itertools import combinations


def kSum(nums: list[int], target: int, k: int) -> list[tuple[int, ...]]:

    def kSum(nums: list[int], target: int, k: int) -> list[tuple[int, ...]]:
        res: list[tuple[int, ...]] = []

        # If we have run out of numbers to add, return res.
        if not nums:
            return res

        # There are k remaining values to add to the sum. The
        # average of these values is at least target // k.
        average_value = target // k

        # We cannot obtain a sum of target if the smallest value
        # in nums is greater than target // k or if the largest
        # value in nums is smaller than target // k.
        if average_value < nums[0] or nums[-1] < average_value:
            return res

        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                new_tuples = list(
                    (nums[i],) + subset for subset in kSum(nums[i + 1:], target - nums[i], k - 1))
                res.extend(new_tuples)

                assert new_tuples == [t for t in
                                      ref(nums, target, k) if t[0] == nums[i]]

        return res

    def twoSum(nums: list[int], target: int) -> list[tuple[int]]:
        res = []
        lo, hi = 0, len(nums) - 1

        assert res == ref(nums[:lo]+nums[hi+1:], target, 2)
        while lo < hi:
            curr_sum = nums[lo] + nums[hi]
            if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append((nums[lo], nums[hi]))
                lo += 1
                hi -= 1

            assert res == ref(nums[:lo]+nums[hi+1:], target, 2)

        return res

    nums.sort()
    return kSum(nums, target, k)


def ref(nums: list[int], target: int, k: int) -> list[tuple[int, ...]]:
    """
    Reference function.
    """
    # Sort the input list to handle duplicates consistently.
    nums.sort()

    # Use itertools.combinations to generate all possible k-tuples.
    result = [combo for combo in combinations(nums, k)
              if sum(combo) == target]

    # Return the list of unique k-tuples.
    return list(tuple(t) for t in sorted(set(result)))


# Example Usage:
test_cases = [
    ([1, 0, -1, 0, -2, 2], 0, 4),  # Example 1
    ([2, 2, 2, 2, 2], 8, 4),       # Example 2
]

for nums, target, k in test_cases:
    assert kSum(nums, target, k) == ref(nums, target, k)
