"""
Issue:
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any
    time.
    However, you can buy it then immediately sell it on the same day. Find and return the maximum profit you can achieve.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.

Solution:
    Method 1:   Because we can buy and/or sell the stock in one day. so every price improve can be added to the
                maximum_profit

    Method 2:   Dynamic Process for each day maximum profit.

"""


def max_profit_m1(prices_list):
    maximum_profit = 0
    for index in range(1, len(prices_list)):
        maximum_profit = max(maximum_profit, maximum_profit + prices_list[index] - prices_list[index - 1])
    return maximum_profit


def max_profit_m2(prices_list):
    dp = [0 for index in range(len(prices_list))]
    for index in range(1, len(prices_list)):
        dp[index] = max(dp[index - 1], dp[index - 1] + prices_list[index] - prices_list[index - 1])
    return dp[-1]


if __name__ == '__main__':
    test_cases = [
        [0], [7, 1, 5, 3, 6, 4], [2, 1]
    ]

    for test_case in test_cases:
        print(f'test_case {test_case} method_1 execute result is {max_profit_m1(test_case)}')
        print(f'test_case {test_case} method_2 execute result is {max_profit_m1(test_case)}')