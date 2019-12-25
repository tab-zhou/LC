# 题目： 求圆周率pi的值
# 思路： 生成坐标系（0，0）（0，2）（2，0）（2，2）四个点围成的正方形中最大的圆是以（1，1）为圆心长度为1的圆，所以
#       圆的面积/正方形面积 = （pi *（1**2））/ 2*2
#       圆的面积/正方形面积可以用概率统计近似得出：即正方形中随机生成点，点坐标与（1，1）距离小于等于1的则落在园内，大于1的落在园外，
#       圆内的计数/总数 近似 圆的面积/正方形面积

import random


def get_pi(times):
    count = 0
    for i in range(times):
        loc_x = random.uniform(0, 2)
        loc_y = random.uniform(0, 2)
        if ((loc_x - 1) ** 2 + (loc_y - 1) ** 2) <= 1:
            count += 1

    return count*(2*2)/times


print(get_pi(10000000))