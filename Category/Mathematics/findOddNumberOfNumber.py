"""
需求：一个整数列表有2个数字出现奇数次，其余数字均出现偶数次，找出这两个数字
思路：1. 由异或整个列表可以找出单个数字出现奇数次的数字 => 把这两个数字分到两个列表中就可以用异或全列表找到.
     2. 如何将两个数字分到2个列表中；a ^ b 之后的二进制数一定不为0，那么从右向左找到第一个为1的位，那么取这一位加上右边的所有0的位组成这个数与
     a和b【相与】结果一定分别一个是0，一个是1 由此可以将两个数区分开
"""


def find_odd_number_of_number(nums):
    # 先得到a^b
    cursor = 0
    for num in nums:
        cursor = cursor ^ num
    # 找到a^b中的最小区别
    index = 0
    while not (cursor & (1 << index)):
        index += 1

    flag_to_divide_list = 1 << index
    # 通过思路2拆分a和b到两个list中
    sub_nums_1 = []
    sub_nums_2 = []

    for num in nums:
        if flag_to_divide_list & num:
            sub_nums_1.append(num)
        else:
            sub_nums_2.append(num)

    result_1 = 0
    result_2 = 0
    for num in sub_nums_1:
        result_1 = result_1 ^ num
    for num in sub_nums_2:
        result_2 = result_2 ^ num

    print(result_1, result_2)


if __name__ == '__main__':
    test_cases = [[1, 1, 2, 2, 3, 5], [1, 2, 3, 4, 5, 3, 2, 1], [1, 1, 2, 2, 1]]

    for test_case in test_cases:
        find_odd_number_of_number(test_case)
