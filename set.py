my_list = ['Kamal', 20, 'Jaffna', False, 20]
my_tuple = ('Kamal', 20, 'Jaffna', False, 20)

my_set = {'Kamal', 20, 'Jaffna', False, 20}
my_set2 = set([20,30,40,50])

# print(my_set) # --> Can only keep unique values. Set is unordered
# print(type(my_set))

# print(my_set2)

my_set.add(123)
print(my_set)

my_set.add((1,2))
print(my_set)

my_set.update((4,"s"))
print(my_set)

my_set.remove(4)
print(my_set)

my_set.discard(False) # Can remove element which is not in the set without error
print(my_set)

my_set.clear() 
my_set.pop() # Remove any element

# print(my_set.union(my_set2))
# print(my_set2.union(my_set))
# print(my_set.intersection(my_set2))
# print(my_set.difference(my_set2))