class AllSubset(object):

    def get_all_subset(self, or_set):
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
test = AllSubset()
for t_index in test_case:
    print(test.get_all_subset(t_index))
