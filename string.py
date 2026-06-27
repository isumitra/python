'''name = "sumitra" 

print(name.upper())  # OUTPUT = SUMITRA
print(name.lower())  # OUTPUT= sumitra


# find a character ....

name = "sumitra Singh"
print(name.find('s')) 

name = "sumitra Singh"
print(name.find('singh'))  # OUTPUT = -1 because small singh not exist.

# next operations...  Replace

name = "sumitra rathore"
print(name.replace("sumitra rathore", "baby singh"))  # OUTPUT= baby singh

# then,

name = "sumitra rathore"
print(name.replace("rathore","singh"))  # OUTPUT = sumitra singh

# replace  character

name = "sumitra rathore"
print(name.replace("s","h"))  # OUTPUT = humitra rathore 

# using in() function


name = "Sumitra rathore"
print('S' in name)  # OUTPUT = true.
print('p' in name)  # OUTPUT = false. because p are no exist in string name.
print('rathore' in name)  # OUTPUT = true.
print('singh' in name)  # OUTPUT = false.


#  escape sequence characters    formating= tab  , next line

str1 = "this is a string. we are creating it in a python."
print(str1)    # output = this is a string. we are creating it in a python

# using \n  this is aescap sequence character.

str1 = "this is a string.\n we are creating it in a python."
print(str1) 

# using  \t  create a space.

str1 = "this is a string.\t we are creating it in a python."
print(str1) 


# operations.

#  1. concatenation

str1 = "sumitra"
str2 = "singh"
final_string = str1+str2
print(final_string)       # output = sumitrasingh


#  2. length of string
 #. len(str) = calculate a string length


str1 = "sumitra"  
len1 = len(str1)
print(len1)

str2 = "singh"
len2 = len(str2)
print(len2)

final_string = str1 + " " + str2  # OUTPUT = 7
# 5
# sumitra singh


print(final_string)
print(len(final_string))     


 # indexing 

str = "sumitra singh"
ch = str[0]
print(ch)

str = "sumitra singh"
ch = str[2]
print(ch)

# or,

str = "sumitra singh"
print(str[3])


# SLICING

str = "sumitra singh"
print(str[1:4])             # output = umi

str = "sumitra singh"
print(str[0:7])              # output = sumitra  

str = "sumitra singh"
print(str[7:len(str)])       # output = singh 


     # str.endswith("ith")

str = "I an studying python form apnacollage"
print(str.endswith("app"))       #output = False 


str = "I am studying python from apnacollage"
print(str.endswith("age"))       # output = true


    # str.capitalize()

str = "i am studying python from apnacollage"
print(str.capitalize()) 

str = "i am studying python from apnacollage"
str = str.capitalize()
print(str) 

    # str. replace(old,new)

str = "I am studying python from apnacollage"
print(str.replace("o","a")) 


str = "I am studying python from apnacollage"
print(str.replace("python","javascript")) 


    # str.find(word)

str = "I am studying python from apnacollage"
print(str.find("o"))      # output = 18

str = "I am studying from python from apnacollage"
print(str.find("from"))    # output = 14

       # str.count

str = "I am from studying python from apnacollage"
print(str.count("from"))    # output = 2

str = "I am studying python from apnacollage"
print(str.count("o"))     # output = 3




# QUESTIONS

# WAP to input user first name and print its length in python.


first_name = input("Enter your first name: ")
print("Length of your first name is : " , len(first_name))

'''

# WAP to find the occurence 's' in a string

str = "Hii, $Iam the $ symbol $99.99"
print(str.count("$"))