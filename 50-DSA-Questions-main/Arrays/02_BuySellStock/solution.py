"""
Problem 2: Best Time to Buy and Sell Stock
Given an array prices where prices[i] is the price of a stock on day i,
find the maximum profit you can achieve from one transaction.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
      """
          Find maximum profit using single pass approach.
              Track minimum price seen so far and calculate potential profit at each step.
                  """
      if not prices:
                return 0

      min_price = float('inf')
      max_profit = 0

    for price in prices:
              min_price = min(min_price, price)
              profit = price - min_price
              max_profit = max(max_profit, profit)

    return max_profit


# Test cases
if __name__ == "__main__":
      # Test Case 1
      prices1 = [7, 1, 5, 3, 6, 4]
      print(f"Input: prices = {prices1}")
      print(f"Output: {maxProfit(prices1)}")  # Expected: 5 (Buy at 1, sell at 6)

    # Test Case 2
      prices2 = [7, 6, 4, 3, 1]
      print(f"Input: prices = {prices2}")
      print(f"Output: {maxProfit(prices2)}")  # Expected: 0 (No profitable transaction)

    # Test Case 3
      prices3 = [2, 4, 1]
      print(f"Input: prices = {prices3}")
      print(f"Output: {maxProfit(prices3)}")  # Expected: 2
