# these are the comments in python script

# Udacity test script for opening a browser at every n secons

import time
import webbrowser

#for var1 in range(1,4):
n = 1 # number of seconds for the break

print("This program started on : "+time.ctime())
temp1 = 0
while (temp1<3):
    time.sleep(n)
    webbrowser.open("https://www.youtube.com/watch?v=Qp6D71kQRhA")
    temp1 = temp1+1
