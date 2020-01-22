# Todo
"""
题目：输出list的全排列
思路：
"""


class FullSort(object):

    @staticmethod
    def full_sort(or_list):
        lenth = len(or_list)
        if lenth <= 1:
            return or_list
        else:
            added_ele = or_list[0]
            new_list = or_list[1::]
            return FullSort.insert(FullSort.full_sort(new_list), added_ele)

    @staticmethod
    def insert(or_list, added_ele):
        result = []
        for i in range(0, len(or_list)+1):
            new_list = or_list[0:i:] + [added_ele] + or_list[i:len(or_list)+1:]
            result.append(new_list)
        return result


test_suite = [[1, 2, 3, 4]]

for test_case in test_suite:
    print(FullSort.full_sort(test_case))