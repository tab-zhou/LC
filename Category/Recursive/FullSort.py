# Todo
"""
需求：输出list的
思路：递归法当前list的全排列等价于依次取出list中数字与剩余list全排列的组合
"""


class FullSort(object):

    @staticmethod
    def full_sort(or_list):
        result = []
        lenth = len(or_list)
        if lenth <= 1:
            return or_list
        else:
            added_ele = [or_list[0]]
            new_list = or_list[1::]
            result += (added_ele + FullSort.full_sort(new_list))
            result += (FullSort.full_sort(new_list) + added_ele)
            return result


    # @staticmethod
    # def full_sort_2(or_list):
    #     lenth = len(or_list)
    #     i = 0
    #     if lenth <= 1:
    #         return or_list
    #     else:
    #         while i < lenth:
    #         return

test_suite = [[1, 2, 3, 4]]

for test_case in test_suite:
    print(FullSort.full_sort(test_case))
