"""
需求：缓存淘汰算法之最近最少使用算法 LRU (Least Recently Used)
     如缓存只能容纳3个数字大小, 按照 6 1 3 2 4 3 5 3 的次序访问
     [][][] > [][][6] > [][1][6] > [3][1][6] > [2][3][1] > [4][2][3] > [3][4][2] > [5][3][4] > [3][5][4]
思路：
"""