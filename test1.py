# test file for python

import mod1
import time

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
