"""
Issue:
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
    future to sell that stock. Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0，
Example:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Solution:
    Method 1: traverse list for each element and the element after it, compare them and calculate the max different
    value. Algorithm Complexity: O(N * logN)
        for index_buy_day in range(0, max_day - 1):
            for index_sell_day in range(index_buy_day + 1, max_day):
                ...
    Method 2:

"""


def cal_maximum_profit(prices_list):
    maximum_profit = 0
    buy_price = prices_list[0]

    for price in prices_list:
        maximum_profit = max(maximum_profit, price - buy_price)
        if price < buy_price:
            buy_price = price

    return maximum_profit


test_cases = [
    [7, 2, 3, 4, 1, 2], [4, 3, 2, 1], [0]
]

if __name__ == '__main__':
    for test_case in test_cases:
        print(f'test_case {test_case} execute result is {cal_maximum_profit(test_case)}')