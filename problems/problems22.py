# Problem: 22 - practice on sets
numbers = {10, 20, 10, 30, 40, 30, 50, 20}
print(numbers)
##Tasks

#1.Common languages
#2.Only Student A knows
#3.Only Student B knows
#4.Total different languages
studentA = {"Python", "Java", "C", "SQL"}

studentB = {"Python", "JavaScript", "SQL", "AI"}

print("common languages:", studentA & studentB)
print("only studentA knows:" , studentA - studentB)
print("only studentB knows:" , studentB - studentA)
print("total diffrent languages:" , studentB | studentA)

#QUESTIONS:

#Python Class

#Java Class

#AI Class

#Find:

#1.ಎಲ್ಲಾ students
#2.Python & Java common
#3.Python & AI common
#4.Java & AI common
#5.ಮೂರು classesಲ್ಲೂ common students
#6.Python ಮಾತ್ರ attend ಮಾಡಿದವರು

python_class = {"A", "B", "C", "D"}

java_class = {"B", "C", "E", "F"}

ai_class = {"C", "D", "F", "G"}

print(python_class| java_class| ai_class )
print(python_class & java_class)
print(python_class& ai_class)
print(java_class& ai_class)
print(java_class& ai_class & python_class)
print(python_class)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1^set2) # symmetric diffrence, elments present in both sets but no common elements

# symmetric diffrence without using operator^
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = (set1-set2)|(set2-set1)
print(result)

#Remove duplicates
#1.Convert to set
#2.Convert back to list
#3.Sort in ascending order
#4.Print only even numbers
numbers = [5,2,8,5,1,2,9,7,8,10]
print(set(numbers))
print(list(numbers))
print(sorted(numbers)) # use sorted



