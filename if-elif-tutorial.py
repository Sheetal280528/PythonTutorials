Lightcolour = input ("colour: ")
if(Lightcolour == "red"):
    print("stop")
elif(Lightcolour == "yellow"):
    print("ready")
elif(Lightcolour == "green"):
    print("go")
else:
    print("signal not working")


food = input("food: ")
eat = "Yes" if food == "cake" else "no"
print("sweet") if food == "cake" or "jalebi" else print("no sweet")

marks = int (input("enter marks "))
if(marks >= 90):
     grade = "A"
elif(marks < 90 and marks >= 80):
     grade = "B"
elif(marks < 80 and marks >= 70):
     grade = "C"
else:
     grade = "D"
print ("grade ", grade)


