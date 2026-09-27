/*
Problem 4: Product of Array Except Self
Time Complexity: O(n), Space Complexity: O(1) excluding output
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
              int n = nums.size();
        vector<int> result(n, 1);

        int prefix = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefix;
            prefix *= nums[i];
        }

        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }
        return result;
    }
};

int main() {
      Solution sol;
    vector<int> nums = {1,2,3,4};
    auto res = sol.productExceptSelf(nums);
    for (int x : res) cout << x << " ";  // 24 12 8 6
    return 0;
}
