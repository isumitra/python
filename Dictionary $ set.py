# Dictionary 
'''
info = {
    "key" : "value",
    "name" : "sumitra",
    "learning" : "python",
    "age" : "22",
    "is_adult" : True,
    "Marks" : 98.4
}

print(info)


info = {
    "name" : "sumitra",
    "subject" : ["python","c++","java"],
    "topics" : ("dist", "set"),
    "age" : "22",
    "is_adult" : True,
    "Marks" : 98.4
}

print(info)


info = {
    "name" : "sumitra",
    "subject" : ["python","c++","java"],
    "topics" : ("dist", "set"),
    "age" : "22",
    "is_adult" : True,
    "Marks" : 98.4
}

null_disk = {}
null_disk["name"] = "sumitra"
print(null_disk)


info["name"] = "baby singh"
print(info)



# Nested dictionary

student = {
    "name" : "sumitra",
    "subject" :{
        "phy" : 98,
        "chem" : 99,
        "bio" : 90
    }

}

print(student)
print(student["subject"])

print(student["subject"]["bio"])




# distionary  methods

# 1. myDict.key

student = {
    "name" : "sumitra",
    "subject" :{
        "phy" : 98,
        "chem" : 99,
        "bio" : 90
    }

}

print(len(student))

print(len(list(student.keys())))


# 2. values()

student = {
    "name" : "sumitra",
    "subject" :{
        "phy" : 98,
        "chem" : 99,
        "bio" : 90
    }

}

print(student.values())
print(list(student.values()))
'''

# 3. items()

student = {
    "name" : "sumitra",
    "subject" :{
        "phy" : 98,
        "chem" : 99,
        "bio" : 90
    }

}

print(student.items())


