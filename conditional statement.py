
 #if-elif-else(SYNTAX)

   if(condition):
        statement1
   elif(condition):
        statement2
   else:
        statementN
   



if(age >= 18):        # if deside on starting condition.
    print("you are an adult")
    print("you can vot") 

print("thank you")



age = 16   # OUTPUT =  YOU ARE in school

if age >= 18:
    print("you are an adult")    # deside on starting condition
    print("you can vot")
elif age < 18 and age > 3:
    print("you are in school")   # starting condition true nhi hoi to ap dusri check kroo nhi to tisri krooo
else:
    print("you are a child")     # agr dono condition false hogi tp hm else m pahuchenge.


print("thank you")       #  yahan bs thank you print hoga q ki adult nhi hai   



age = 2  # OUTPUT =  YOU ARE A CHILD

if age >= 18:
    print("you are an adult")    
    print("you can vot")
elif age < 18 and age > 3:
    print("you are in school")  
else:
    print("you are a child")     


print("thank you")       



age = 19  # OUTPUT =  YOU ARE An AUDELT     YOU CAN VOT   THANK YOU.

if age >= 18:
    print("you are an adult")    
    print("you can vot")
elif age < 18 and age > 3:
    print("you are in school")  
else:
    print("you are a child")     


print("thank you")     




# RANGE   IS A KEYWORD

number = range(5)
print(number)       # OUTPUT = (0,5)







age = 24

if(age >= 18):
  print("can vote")
  print("can drive")




light = "green"

if(light == "red"):
  print("stop")
elif(light == "green"):
  print("go")
elif(light == "yellow"):
  print("look")  

print("End of code")


light = "green"

if(light == "red"):
  print("stop")
if(light == "green"):
  print("go")
if(light == "yellow"):
  print("look")  

print("End of code")



light = "pink"

if(light == "red"):
  print("stop")
elif(light == "green"):
  print("go")
elif(light == "yellow"):
  print("look")  
else:
  print("light is broken")

print("End of code")


age = 18

if(age >= 18):
  print("can vote")
else:
  print("can not vote")

age = 14

if(age >= 18):
  print("can vote")  #indendataion {}
else:
  print("cannot vote")



#pratices question

marks = 78

if(marks >= 90):
  grade = "A"
elif(marks >= 80 and marks < 90):
  grade = "B"
elif(marks >= 70 and marks < 80):
  grade = "C"
else:
  grade = "D"

print("grade of the student =" , grade)



marks = int(input("Enter student marks :"))

if(marks >= 90):
  grade = "A"
elif(marks >= 80 and marks < 90):
  grade = "B"
elif(marks >= 70 and marks < 80):
  grade = "C"
else:
  grade = "D"

print("grade of the student =" , grade)


# NESTING

age = 34

if(age >= 18):
  if(age >= 80):
    print("cannot drive")
  else:
    print("can drive")
else:
  print("cannot drive")  



age = 95

if(age >= 18):
  if(age >= 80):
    print("cannot drive")
  else:
    print("can drive")
else:
  print("cannot drive")      



  #practic  questions

num = int(input("Eneter the number :"))

rem = num % 2

if(rem == 0):
  print("Even")
else:
  print("odd")  




a = int(input("Eneter the first number:"))
b = int(input("Eneter the second number:"))
c = int(input("Eneter the third number:"))

if(a >= b and a >= c):
  print("first number is largest",a)
elif(b >= c):
  print("second number is largest",b)
else:
  print("third number is largest",c)    




a = int(input("Eneter the first number:"))
b = int(input("Eneter the second number:"))
c = int(input("Eneter the third number:"))
d = int(input("Eneter the fourth number:"))

if(a >= b and a >= c and a >= d):
  print("first number is largest",a)
elif(b >= a and b >= c and b >= d):
  print("second number is largest",b)
elif(c >= a and c >= b and c >= d):
  print("third number is largest",c)  
else:
  print("fourth number is largest",d)    



x = int(input("Enter number:"))

if(x % 7 ==0):
  print("multiple of 7")
else:
  print("not a multiple:")



