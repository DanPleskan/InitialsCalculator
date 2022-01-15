from datetime import datetime
import os
now = datetime.now() #getting the date and time module
def get_string():
    return input("Input full name please: ")
def display(person):
    check=1
    count=0
    for i in person:
        if ord(i)==32:
            check=1
        if ord(i)!=32 and check==1:
            print("%s."%i, end=' ')
            check=0
            count+=1
        if count==3:
            break

person=get_string()

#print person initials
display(person)
