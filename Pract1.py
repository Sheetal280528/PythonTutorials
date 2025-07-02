str1 = "we are in office. I want to leave now."
print (str1)
# we are in office. I want to leave now.
str2 = "we are in office.\nI want to leave now."
print(str2)
#we are in office.
#I want to leave now.        ---> creating new line using \n
str3 = "we are in office.\tI want to leave now."
print(str3)
#we are in office.       I want to leave now. ---> creating a tab using \t

#String Concatat using +
print (len(str1)) #38
print (len(str2)) #38
print (len(str3)) #38

str = "Apna_Call"
print (str)
print (len(str)) #9
#indexing: using index we can access values of string but can not changes it
# String is immutable
print (str[0])   #A
print (str[1])   #p

#slicing
# A  p  n  a  _  C  a  l  l
# 0  1  2  3  4  5  6  7  8
#-9 -8 -7 -6  -5 -4 -3 -2 -1
print (str[1:4]) #pna
print (str[0:3]) #Apn   ---> ending index - 1 position
print (str[4:len(str)]) 

#len is 9 so till 8th position so the output is _Call
print (str[4:])        # if we miss on ending index value then it is implictly considers the length, output is _Call
print (str [:5])       # automatically starting index will be conisdered zero so output is Apna_
#Revers Indexing end point is -1 and then in reverse order 

print (str [-5:-1])    # _Cal

str1 = "hello World"
print (str1.endswith("app")) # False
print (str1.endswith("ld"))  #True
print (str1.capitalize())    # starting letter will be capital so output is Hello world
print (str1)                 # prinst original string i.e. hello World
str1 = str1.capitalize()
print (str1)                 # after assigning capital string to original now output Hello world
print (str1.replace("l","s")) # replacing "l" by "s" --> Hesso worsd
print (str1.replace("Hello","Hi"))  #latest string is "Hi world"
print (str1)
print (str1.find("o"))  #output is 4 ---> in Hello World string "o" is found at 4th position
print (str1.count("l")) #output is 3 ---> "l" is 3 times in string

str2 = "I LOVE U AYANSH"
print (str2.center(20,"#")) ###I LOVE U AYANSH###
print (str2.capitalize()) #I love u ayansh
print (str2.casefold())  #i love u ayansh
print(len("###I LOVE U AYANSH###")) #21


