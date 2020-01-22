"""
题目：返回集合所有的子集
思路：{1}的子集为[{},{1}]->(0,1)，{1,2}的子集为[{},{1},{2},{1,2}]->(00,01,10,11)，可得出结论，集合的子集数为2**N，子集中元素的取
     值正好匹配2**N的二进制标志，0为不取，1为取,所以该问题转化为展示2**N 和对应位置取值的问题

"""

class AllSubset(object):

    @staticmethod
    def get_all_subset(or_set):
        count = len(or_set)
        all_sub_set = []
        for i in range(2 ** count):
            sub_set = []
            for j in range(count):
                if (i >> j) % 2 == 1:
                    sub_set.append(or_set[j])
            all_sub_set.append(sub_set)
        return all_sub_set


test_case = [[1, 2, 3, 4]]
for t_index in test_case:
    print(AllSubset.get_all_subset(t_index))
