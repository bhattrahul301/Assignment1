def last(l):
    return l[-1]

def sort_last(tuples):
    return sorted(tuples, key=last)

print(sort_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
