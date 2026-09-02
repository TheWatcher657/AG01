"""
lets make a attendance system for the students and save the result in an csv

"""

import csv
def attendaceSheet():
    """ this function is to take the records of the student and insert them into an array"""
    attendance =[]
    a = int(input("how many students"))
    for i in range(a):
        name = input(f"enter the name of the {i+1} student : ")
        rollNo = int(input("enter thier roll no "))
        present = input("present a/p: ")
        attendance.append([name,rollNo,present])
    return attendance



def saveCsv(attendace):
    """ the use of this function is to take the array and put it in the csv file"""
    with open("attendance.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["studentsName","rollNo","presentOrAbsent"])
        writer.writerows(attendace)
    print("----saved---- good job harsh")

data = attendaceSheet()
saveCsv(data)