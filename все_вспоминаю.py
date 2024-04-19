



numbers_list = []
for i in range(11):
    numbers_list.append(i)

numbers_list_ordered = numbers_list.copy()
numbers_list_ordered.sort(reverse=True)


numbers_set = set(numbers_list)
max_numbers_list = max(numbers_list)
numbers_set.add(max_numbers_list)


numbers_list = [1,2,3,4]
max_numbers_list = max(numbers_list)

numbers_frozenset = set(numbers_list)
min_numbers_list = min(numbers_list)
numbers_frozenset.remove(max_numbers_list)


