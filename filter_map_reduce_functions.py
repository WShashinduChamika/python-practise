from functools import reduce

number = [1,2,3,4,5,6,7,8]

def even_num(x):
    return x  % 2 == 0

y = list(filter(even_num, number))
print(y)

z = list(filter(lambda x: x%2 == 0, number))
print(z)

# Map Function
a = list(map(lambda x: x*2, number))
print(a)

# Reduce Function
sum = reduce(lambda x, y : x+y, number)
print(sum)
