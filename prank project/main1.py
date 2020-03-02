import os


# This is the prank project from udacity course


print("Udacity Prank Project- renaming files")

# Defining a function first

def rename_files():
    # Get file names from a folder
    path = "/Users/singh281/Desktop/Scripts/Python test/prank project/prank/"
    dirs = os.listdir(path)
    #print(dirs[])  #, printing all the elements of the string array dir

    temp1 = 0
    str2 = ".jpg"
    dir1=[]  # initializing a string array here
    for str1 in dirs:
        if str2 in str1:
            #print("found")
            dir1.append(str1)
        temp1 = temp1+1

    os.chdir("/Users/singh281/Desktop/Scripts/Python test/prank project/prank/")
    saved_path = os.getcwd()
    print("Current working directory is: "+ saved_path)

    # Change the file names
    for file_name in dirs:
        os.rename(file_name,file_name.translate(None, '0123456789'))

    # return statements here
    return()


var1 = rename_files()
#print(var1)
