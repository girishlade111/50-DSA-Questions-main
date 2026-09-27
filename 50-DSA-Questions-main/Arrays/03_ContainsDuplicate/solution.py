"""
Problem 3: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice,
and return false if every element is distinct.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
      seen = set()
      for num in nums:
                if num in seen:
                              return True
                          seen.add(num)
            return False


if __name__ == "__main__":
      print(containsDuplicate([1,2,3,1]))  # True
    print(containsDuplicate([1,2,3,4]))  # False
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True
