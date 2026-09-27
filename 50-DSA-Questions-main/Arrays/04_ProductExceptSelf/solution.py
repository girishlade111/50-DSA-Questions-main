Arrays/04_ProductExceptSelf/solution.py"""
Problem 4: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].
Time Complexity: O(n), Space Complexity: O(1) (excluding output array)
"""

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # Left pass - calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Right pass - multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))  # [24,12,8,6]
    print(productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
