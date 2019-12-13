class MaxCapacity(object):

    def maxArea(self, container) -> int:
        head_point = 0
        end_point = len(container)-1
        max_area = 0
        area_lenth  = end_point - head_point
        while area_lenth:
            height_head = container[head_point]
            height_end = container[end_point]
            height = min(height_head, height_end)
            if max_area <= height * area_lenth:
                max_area = height * area_lenth

            if height_head >= height_end:
                end_point -= 1
            else:
                head_point += 1
            area_lenth = end_point - head_point
        return max_area
