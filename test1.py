# test file for python

import mod1
import time
import os
import sys
import string

print(2+5)
print("hello world")

var1 = 4+8
print(var1)

# Using a function from an imported module here

mod1.print_fun("Zara")

# simple for loop in python

for var1 in range(1,3):
    print(var1)
    print("test statement here")
    #mod1.print_fun(var1)

print("End of the loop here")
#print("hey there what do you want?")

print("===================================")

# Testing the time module in python
var2 = time.ctime()
print(var2)

# Simple function definition in python
print("========== Function Testing ==============")

def testfun1(temp1,temp2):
    temp3 = temp1+temp2
    print("Adding the two numbers now")
    print("The final result is " + str(temp3))
    #return(temp3)
   # The command return is not needed in python necessarily

var3 = testfun1(2,234)
#print(var3)

# Testing some strings operations there
print("========== String operations Testing ==============")
# Deleting characters from a string

str1 = ["temp123"]
#print(str1[0])
str2 = str1[0]

str2 = str2.translate(None, "123")
print(str2)
