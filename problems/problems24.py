# problem: 24 "dictionary 2"

#problem 1 - dictionary + access

information = {"name" : "nagaraj",
               "age" : 18,
               "branch" : "aiml",
               "city" : "bangalore"}
print(information["name"])
print(information["branch"])

'''Problem 2 - Add & Update Dictionary'''
student = {
    "Name": "Nagaraj",
    "Age": 18,
    "Branch": "AIML"
}

student["city"] = "banglore"
print("adding city to list")
print(student)
print("updating")
student["age"] = 19
print(student)

# problem 3 :Print Student Details

student = {
    "Name": "Nagaraj",
    "Age": 19,
    "Branch": "AIML",
    "City": "Bangalore"
}

print(student.keys())
print(student.values())
print(student)
for key in student: # ee function use madodh yavag namig keys one by one bekagutto avaga
    print(student[key])
