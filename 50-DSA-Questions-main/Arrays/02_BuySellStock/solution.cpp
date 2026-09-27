/*
Problem 2: Best Time to Buy and Sell Stock
Given an array prices where prices[i] is the price of a stock on day i,
find the maximum profit you can achieve from one transaction.

Time Complexity: O(n)
Space Complexity: O(1)
  */

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
              if (prices.empty()) return 0;

        int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            minPrice = min(minPrice, price);
            int profit = price - minPrice;
            maxProfit = max(maxProfit, profit);
        }

        return maxProfit;
    }
};

int main() {
      Solution sol;

    // Test Case 1
    vector<int> prices1 = {7, 1, 5, 3, 6, 4};
    cout << "Input: prices = [7,1,5,3,6,4]" << endl;
    cout << "Output: " << sol.maxProfit(prices1) << endl;
    // Expected: 5

    // Test Case 2
    vector<int> prices2 = {7, 6, 4, 3, 1};
    cout << "Input: prices = [7,6,4,3,1]" << endl;
    cout << "Output: " << sol.maxProfit(prices2) << endl;
    // Expected: 0

    return 0;
}
