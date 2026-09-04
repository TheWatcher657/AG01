"""
while 

while condition :
    instruction
    something that will the conditon false

# """
# # a = int(input(" eneter the number of subject you have"))
# # i=0
# # total =0
# # while i<a :
# #     d = int(input("Enter you total marks : "))
# #     total = total + d
#     i = i+1
#  print (total)     

a = int(input(" enter the number of subject you have"))
total = 0
while a>0:
    d = int(input(f" enter the marks of your {a} subject : "))
    total = total + d #total = 65(current value of total) + 45(d value) 65+45 will make the new total value
    a = a-1
print(total)    

"""
for i in range(5):
    print(i)
"""


# for i in "harsh":
#     print (i)   


for i in range(20):
    if i%2==0:
        print(str(i) + "even")
    else:
        print(str(i) + "odd")    


# a = int(input( " enter the range of your number "))
# for i in range(a):
#     if i%3==0:
#         print(i,"fizz")
#     elif i%5==0:
#         print(i,"fuzz")    

for i in range(5):
    print(i)



