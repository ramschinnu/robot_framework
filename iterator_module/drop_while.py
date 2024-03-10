import itertools
# initializing list
list1 = [2, 4, 5, 7, 8,10,12,14]
# using dropwhile() iterator that will print start displaying after condition is false
print("The output is : ", end="")
print(list(itertools.dropwhile(lambda x: x % 2 == 0, list1)))