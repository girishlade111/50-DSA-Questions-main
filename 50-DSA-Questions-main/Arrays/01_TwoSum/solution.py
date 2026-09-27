"""
Problem 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
      """
          Find two numbers that add up to target using hash map approach.

                  Args:
                          nums: List of integers
                                  target: Target sum

                                              Returns:
                                                      List containing indices of two numbers that add up to target
                                                          """
      num_map = {}  # value -> index

    for i, num in enumerate(nums):
              complement = target - num
              if complement in num_map:
                            return [num_map[complement], i]
                        num_map[num] = i

    return []  # No solution found


# Test cases
if __name__ == "__main__":
      # Test Case 1
      nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {twoSum(nums1, target1)}")  # Expected: [0, 1]

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {twoSum(nums2, target2)}")  # Expected: [1, 2]

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {twoSum(nums3, target3)}")  # Expected: [0, 1]
