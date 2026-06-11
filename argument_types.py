# # Positional arguments
# def student_info(name,age):
#     print(f"My name is {name}. My age is {age}")

# student_info('Shashindu', 12)

# # Key word argument
# def student_info2(name,age, gender):
#     print(f"My name is {name}. My age is {age} and gneder is {gender}")

# student_info2('Shashindu', gender=6, age=12)

# Variable length function
# def cal_total_marks(mark1, mark2, mark3):
#     total = mark1 + mark2 + mark3
#     print(total)

# def cal_total_marks(*args):
#     total = 0
#     for mark in args:
#         total += mark
#     print(total)

# cal_total_marks(87,56)

def cal_total_marks(**kwargs):
    total = 0
    for mark in kwargs.values():
        total += mark
    print(total)

cal_total_marks(math=87,scinece=56)