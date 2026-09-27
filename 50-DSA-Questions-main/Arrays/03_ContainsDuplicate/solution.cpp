/*
Problem 3: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice.
Time Complexity: O(n), Space Complexity: O(n)
  */

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
              unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) return true;
            seen.insert(num);
        }
        return false;
    }
};

int main() {
      Solution sol;
    vector<int> nums1 = {1,2,3,1};
    vector<int> nums2 = {1,2,3,4};
    cout << boolalpha << sol.containsDuplicate(nums1) << endl;  // true
    cout << sol.containsDuplicate(nums2) << endl;  // false
    return 0;
}
