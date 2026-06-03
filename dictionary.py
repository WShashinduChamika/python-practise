my_dict = {'name':'Shashindu', 'age':20, 'city':'Kandy'}
students = {80:'Kamal', 81:'Sathira'}

print(my_dict)
print(type(my_dict))

my_dict['name'] = 'Cha'

print(my_dict)

my_dict['is_married'] = False

print(my_dict)

my_dict.update({'is_married':False, 'gender':'male'})

print(my_dict)

print(my_dict.pop('name'))

print(my_dict.pop('xyz', 'Not found'))

print(my_dict.clear())