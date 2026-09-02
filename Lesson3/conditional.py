#
#if condition :
#    instruction
# a = 34
# b = int(input("guess a number : "))
# if a==b:
#     print("correct")
# else : 
#     print("bad luck")

a = input("enter you name : ")
b = int(input("enter your age : "))
c = input("Do you have a ID y/n : ")

if c == "y":
    d = int(input("Enter you total marks : "))
    if d > 90 :
        print("good job "+ a + " you are selected for scholorship")
    elif d>80 and d<91 :
        print("good job "+ a +" but we regret to inform you that you are not given the money")

    else : print("you are not selected")



