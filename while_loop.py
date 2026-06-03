# i = 0
# while(i<6):
#     print(i)
#     i += 2


numbers = []
sum = 0
i = 1

while (i<=5):
    num = int(input(f'Enter number {i} : '))
    sum += num
    i += 1

print(f"Sum of five numbers is {sum}")