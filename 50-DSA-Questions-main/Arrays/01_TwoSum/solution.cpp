/*
Problem 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

  Time Complexity: O(n)
  Space Complexity: O(n)
  */

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
              unordered_map<int, int> numMap;  // value -> index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }

            numMap[nums[i]] = i;
        }

        return {};  // No solution found
    }
};

// Test cases
int main() {
      Solution sol;

    // Test Case 1
    vector<int> nums1 = {2, 7, 11, 15};
    int target1 = 9;
    vector<int> result1 = sol.twoSum(nums1, target1);
    cout << "Input: nums = [2,7,11,15], target = 9" << endl;
    cout << "Output: [" << result1[0] << ", " << result1[1] << "]" << endl;
    // Expected: [0, 1]

    // Test Case 2
    vector<int> nums2 = {3, 2, 4};
    int target2 = 6;
    vector<int> result2 = sol.twoSum(nums2, target2);
    cout << "Input: nums = [3,2,4], target = 6" << endl;
    cout << "Output: [" << result2[0] << ", " << result2[1] << "]" << endl;
    // Expected: [1, 2]

    // Test Case 3
    vector<int> nums3 = {3, 3};
    int target3 = 6;
    vector<int> result3 = sol.twoSum(nums3, target3);
    cout << "Input: nums = [3,3], target = 6" << endl;
    cout << "Output: [" << result3[0] << ", " << result3[1] << "]" << endl;
    // Expected: [0, 1]

    return 0;
}
