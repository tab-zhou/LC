from itertools import product


class AllSubset(object):
    def __init__(self):
        self.ext = []

    @classmethod
    def get_all_subset(cls, or_set: set):
        result = [set()]
        ext = []
        ext_list = []
        while or_set != set():
            ext.append(or_set.pop())
            for j in ext:
                for i in result:
                    ext_list.append({i.add(j)})
            result = result + ext_list
        return result


test_case = [{1, 2}]
test = AllSubset()
for t_index in test_case:
    print(test.get_all_subset(t_index))
