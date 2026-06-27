'''#  LIST   (collection of items  , it is complex datatype ,[] used this )
#  It can store elements of differents types(integer,float,string,etc)

marks = [95,98, 97]
print(marks)          # 95, 98, 97

marks = [95,98, 97]
print(marks[1])       #  98

marks = [95,98, 97]
print(marks[0])       # 95


marks = [95,98, 97]     
print(marks[-1])       #  97

marks = [95,98, 97]
print(marks[-2])      #  98


marks = [95,98, 97]
print(marks[1:2])   #[98]


marks = [95,98, 97]
print(marks[0:2])   #[95,98]


marks = [95,98, 97]
print(marks[1:3])      #[98,97]

# using loop 

marks = [95,98, 97]

for score in marks:
    print(score)

    #  APPEND OPERATION

marks = [95,98, 97]

marks.append(99)
print(marks)        # [95,98,97,99]

     #  INSERT  OPERATION

marks = [95,98, 97]
marks.insert(0,99)
print(marks)





marks = [92.7, 98.9, 99.9, 87.6, 98.6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])


marks = [92.7, 98.9, 99.9, 87.6, 98.6]
print(marks)
print(len(marks))


student = ["sumitra", 95.6, "bihar"]
print(student)


Str = "hello"
print(str[0])
str[0] = "y"    


student = ["sumitra", 98.6, "bihar"]
print(student[2])
student[2] = "up"
print(student)   


# slysing

marks = [87, 98, 99, 65]
print(marks[1:3])

# negative index

marks = [87, 98, 99, 65]
print(marks[-3:-1])


# List methods
# 1. append

list = [2, 1, 3]
list.append(4)
print(list)

# 2. shot method

list = [4, 2, 3]
print(list.append(5))
print(list.sort())
print(list)

list = ["banana","litchi","apple"]
#print(list.append(5))
print(list.sort())
print(list)

list = ['e','d','b','e','c','a']
#print(list.append(5))
print(list.sort())
print(list)

#  Desending order


list = [4, 2, 3]
print(list.append(5))
print(list.sort(reverse=True))
print(list)

list = ["banana","litchi","apple"]
#print(list.append(5))
print(list.sort(reverse=True))
print(list)

list = ['e','d','b','e','c','a']
#print(list.append(5))
print(list.sort(reverse=True))
print(list)


# Insert Method

list = [2, 1, 3]
list.insert(1, 5)
print(list)

# Remove Method

list = [2, 1, 3, 1]
list.remove(1)
print(list)
'''
list = [2, 1, 3, 1]
list.pop(2)
print(list)
