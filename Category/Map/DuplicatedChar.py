# 题目： 输出任意字符串中只出现一次的字符
# 思路： 新建一个dict 存储每个字符出现的次数，最后输出所有次数为1的字符


class DuplicatedChar(object):
    @staticmethod
    def duplicated_char(or_string):
        map_dict = {}
        result = []
        for i in or_string:
            if map_dict.get(i):
                map_dict[i] += 1
            else:
                map_dict[i] = 1

        for i in or_string:
            if map_dict.get(i) == 1:
                result.append(i)

        return result


test_suites = ['adsadsfa123', '']

for test_case in test_suites:
    print(DuplicatedChar.duplicated_char(test_case))
