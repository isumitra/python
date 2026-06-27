# Tupple 
'''
tup = (2, 4, 7, 9)
print(tup[0])
print(tup[1])

tup = (1)  # int
print(tup)
print(type(tup))

tup = (1.3)  # float
print(tup)
print(type(tup))

tup = ("sumitra")  # str
print(tup)
print(type(tup))

# slysing

tup = (2, 4, 6, 7)  
print(tup[1:3])

# METHOD

#1.tup.index( el )

tup = (1,2,3,4)
print(tup.index(2))

# 2. tup.count( el )

tup = (1,2,3,4)
print(tup.count(2))

tup = (1,2,3,4,2,2)
print(tup.count(2))



# Q1.wap to ask the user to enter names of their 3 favorite movies & store them in a list

movies = []
mov1 = input("Enter the 1st movies :")
mov2 = input("Enter the 2nd movies:")
mov3 = input("Enter the 3rd movies:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# or,

movies = []
mov = input("Enter 1st movie: ")
movies.append(mov)
mov = input("Enter 2ed movie: ")
movies.append(mov)
mov = input("Enter 3rd movie: ")
movies.append(mov)

print(movies)


# or,

movies = []
movies.append(input("Enter 1st movie:"))
movies.append(input("Enter 2ed movie:"))
movies.append(input("Eneter 3rd movie:"))
print(movies)


# Q2.WAP to check if a list contains a palindrome of elements. (hint: use copy method)

list1 = [1,2,1]
list2 = [1,2,3]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("palidrome")
else:
    (" nott palidrome")



list1 = [1,2,3]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("palidrome")
else:
    ("not palidrime")


    #Q 3 . WAP to count a number of students with the "A" grade in the following tupple.

grade = ("c", "d", "a", "a", "b", "b", "a")
print(grade.count("a"))    
'''

# Q4. store yhe above value in a list $ sort them "A" to "D".

grade = ["c", "d", "a", "a", "b", "b", "a"]
grade.sort()
print(grade)    
