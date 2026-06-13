x = int(input('Enter number'))

result = 1

for i in range(1,x+1):
    result *= i

print(result)


def fact(n):
    if n==0:
        return 1
    else: 
        return n * fact(n-1)

