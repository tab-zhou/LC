"""
需求： 给出n对括号，求括号排列的所有可能性
思路： 主要是尝试使用回溯法
"""


class BracketMapping(object):
    result = []

    @staticmethod
    def mapping(sub_result, result, left_count, right_count):
        if left_count == 0 and right_count == 0:
            return result.append(sub_result)
        if right_count > left_count:
            BracketMapping.mapping(sub_result + ')', result, left_count, right_count-1)
        if left_count > 0:
            BracketMapping.mapping(sub_result + '(', result, left_count-1, right_count)


test_suite = [2]
for test_case in test_suite:
    print(BracketMapping.mapping('', [], test_case, test_case))