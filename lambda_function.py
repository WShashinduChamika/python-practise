square_area = lambda x : x * x

rectange_area = lambda x,y : x * y

print(square_area(5))
print(rectange_area(5,7))

def apple(unit_price):
  price = lambda number_of_apples : number_of_apples * unit_price
  return price

total_price = apple(40)
print(total_price(2))

