def student(subject="Maths", marks=35, *friends):
    print("Subject = ", subject)
    print("Marks  = ", marks)
    print("Friends = ", friends)

student("Art", 50, 'Saman','Sunil')

def student2(subject="Maths", marks=35, **friends):
    print("Subject = ", subject)
    print("Marks  = ", marks)
    
    for key,value in friends.items():
        print(key,value)

student2("Art", 50, Saman=25,Sunil=35)
