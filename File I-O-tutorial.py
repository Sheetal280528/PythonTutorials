# Types of Files: 
#Text File (which stores data in Characters)--- .txt, .docx, .log etc
#Binary File (which stores data in bytes)   --- .mov, .png, .jpeg, .mp4 etc
#but ultimately when we use these files in program both will store data in 0 or 1 which is bits

### reads the entire data of the file
file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo.txt", "r")
line1 = file1.readline()  ###it prints the first line and then an empty line bcz of \n char which is present at the last of 1st line
print(line1)
line2 = file1.readline()  
print(line2)
data1 = file1.read()      #this will print the remaining entire stuff in file (starts reading from where the previous read is completed)
print(data1)
print(type(data1))
file1.close()

#reads the number of characters only (number is passed in argument of read)
file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo.txt", "r")
data1 = file1.read(3)
print(data1)
data2 = file1.readline(2) #readline reads one line at a time and if pass any number in argument so it reads those chars only
print(data2)
file1.close()


#reads the number of characters only (number is passed in argument of read)
#if we use "w" or "a" mode and the file doesnt exist then python will create that file for us
file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo.txt", "w")
file1.write("I am writing this file which will overwrite the existing data")
file1.close()

file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo.txt", "a")
file1.write("now I am trying to append the data thru mode a")
file1.write("\n bcz my previous append data was appeneded in existing line")
file1.close()

file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo.txt", "r")
data1 = file1.read()     
file1.close()

file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo1.txt", "a")
file1.write("now I am trying to append the data thru mode a but file doesnt exist")
file1.write("\n bcz my previous append data was appeneded in existing line")
file1.close()


#"r+ mode": starts cursor position from the starting point so if we write first then due to cursor position it will start overwriting from first. 
# If now we give read command then it starts reading from where this writing was stopped and cursor was positioned
file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo1.txt", "r+")
file1.write("now I am trying to append the data thru mode a")
file1.write("\n bcz my previous append data was appeneded in existing line")
file1.close()

file1 = open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo.txt", "r")
data1 = file1.read()     
file1.close()

### WITH OPENS
with open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo1.txt", "r") as file1:
    data = file1.read()
    print("with open trial")
    print("***************")
    print(data)
##this doesn't need to close the file

##deleting the file
#import os
#os.remove("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo1.txt")


###try replacing few words in file
### first write a file
with open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo2.txt","w") as file1:
    file1.write("I love Java\nI want to learn Java\nbut I don't know how to start Java study")
with open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo2.txt","r") as file1:
    data1 = file1.read()
    print(data1)
newdata = data1.replace("Java", "Python")
print(newdata)
with open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo2.txt","w") as file1:
    file1.write(newdata)
with open("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo2.txt","r") as file1:
    data2 = file1.read()
    print("new data\n", data2)


### try to create function to find word Python in file, its place & count
def word_search():
    word = "Python"
    with open ("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo2.txt","r") as f1:
        data = f1.read()
        print("data for search", data)
        index = data.find(word) 
        if (index != -1):
            print("word found at ", index)
        else:
            print("not found")
        count1 = data.count(word)
        print("words is found ", count1, "times")
       
word_search()

### try creating function to find any word plus in which line the word is present
def word_line_search():
    word = "shell"
    data = True                  
#this is declared bcz while reading the file at the end we might end up having spaces so how would we come to know that the data of the file is finished
#so until the data = True we have valid data in this variable
    line_num = 1
    with open ("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Demo2.txt","r") as f1:
         while data:
             data = f1.readline()
             if (word in data):
                 print("word is found at line number", line_num)
                 line_num = line_num + 1
             else:
                 print("sorry no word found")
                 return -1                    #if you want to print -1 when word is not found then return -1 and print function call
 
print(word_line_search())

###print the even numbers from the file of numbers seperated by ,
count = 0
with open ("C:\\Users\\sr93628\\OneDrive - Deere & Co\\Desktop\\Python\\Untitled-1.py","r") as f2:
    data = f2.read()
    print(data)
    num_list = data.split(",")
    print(num_list)
    for el in num_list:
        if (int(el)%2 == 0):
            print(el, "number is even")
            count = count + 1
        else:
            print(el, "number is odd")
    print("total even numbers ", count)
