#!/usr/bin/python3

def uniq_add(my_list=[]):
    nlist = set(my_list)
    return sum(nlist)

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
