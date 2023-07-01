# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/random.html#functions-for-integers
# https://docs.python.org/3/library/random.html#functions-for-sequences
# Dr. Angela Yu - 100 Days of Code:  
# The Complete Python Pro Bootcamp for 2022Python-100days-Angela Yu
# https://www.w3schools.com/python/module_random.asp
# https://www.geeksforgeeks.org/python-programming-language/?ref=ghm
# https://www.hackerrank.com/domains/python



# exit() is considered bad to use in production code because it relies on site module.
# sys.exit() good to use in production code because the sys module will always be there.
# https://pythonguides.com/python-exit-command/
# https://stackoverflow.com/questions/16656313/exit-while-loop-in-python

import random
import string
import sys

# variables
# depatment - department names
# number    - how many EC2 instances they want names for


def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))


department = input("Enter Department: Marketing, Accounting, FinOps: ")  
    
for _ in department:
    
    if department == "Marketing" or department.lower() == "marketing" :
        print("Ok to go")
        #print ("Marketing")
        break
    
    elif department == "Accounting" or department.lower() == "accounting" :
        print("OK to go")
        #print("Accounting")
        break
    
    elif department == "FinOps" or department.lower() == "finops" :
        print("OK to go")
        #print("FinOps")
        break
    
    else:
        print("Error: You can not use this generator, enter the name correctly.")
        raise SystemExit
        sys.exit()  

        
number = int(input("Enter the number of EC2 instances you need: "))


    
if number < 0:
    print("Please enter a positive number: ")
 
elif number > 0:
    print("Good to go")
    
   
        

print()
print("--------------------------------")
print("EC2 Instance Names")
print("--------------------------------")
print()

for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = unique_name + "-" + string_generator()
    print("Your EC2 Instance's unique name is : ", EC2_unique_name)
    
