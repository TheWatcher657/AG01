"""
def function_name():
    instruction 

"""

# def greet():
#     print("hello")

# greet()    

# def greet(name):
#     print("hello",name)

# greet("harsh")

# def sum(a,b):
#     print(a+b)

# def sum2(a,b):
#     return(a+b)

# sum(2,4)
# a =sum2(2,4)
# print(a)

def takeMarks(a):
    total = 0
    for i in range(a):
        b = int(input(f"marks of subject {i}: "))
        total = total + 1
        i+=1
    return total    

def greet(a):
    return f"hello {a}" 

name = input("enter you name : ")
total_subject = int(input(" enter your total subject")) 
print(greet(name),"your total marks is  ",takeMarks(total_subject))