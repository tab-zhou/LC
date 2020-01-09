"""
题目：给出一个list，元素值代表高度，求出list中任意两个元素围成面积最大的情况
思路：基本方法-双重遍历：从开始-结尾遍历出所有N to N+X的面积，时间复杂度f(n**2)
     双指针：因为随着指针的趋近，下边一定是在缩短的，高度取决于较短边，所以要移动较短边才有可能使面积增大，所以只要移动两个边之间较短边直
     到两个边重合，过程中最大的面积即为最大面积，时间复杂度将为f(n)
"""


class MaxCapacity(object):

    @staticmethod
    def max_area(container) -> int:
        head_point = 0
        end_point = len(container)-1
        max_area = 0
        area_length = end_point - head_point
        while area_length:
            height_head = container[head_point]
            height_end = container[end_point]
            height = min(height_head, height_end)
            if max_area <= height * area_length:
                max_area = height * area_length

            if height_head >= height_end:
                end_point -= 1
            else:
                head_point += 1
            area_length = end_point - head_point
        return max_area


test_case = [[1, 2, 3, 4, 5], [1, 8, 13, 4, 9], [0, 0, 0, 0], [1, 1]]
test = MaxCapacity()
for i in test_case:
    print(test.max_area(i))
