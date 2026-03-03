some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#find duplicates in the given list using list comprehension
duplicates = list(set([char for char in some_list if some_list.count(char)>1]))
print(duplicates)
