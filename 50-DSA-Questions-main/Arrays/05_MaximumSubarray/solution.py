"""
Problem 5: Maximum Subarray (Kadane's Algorithm)
Find the contiguous subarray with the largest sum.
Time Complexity: O(n), Space Complexity: O(1)
"""

from typing import List

def maxSubArray(nums: List[int]) -> int:
      max_sum = nums[0]
      current_sum = nums[0]

    for i in range(1, len(nums)):
              current_sum = max(nums[i], current_sum + nums[i])
              max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
      print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6 ([4,-1,2,1])
    print(maxSubArray([1]))  # 1
    print(maxSubArray([5,4,-1,7,8]))  # 23
