# topic : tuples and sets
## NOTE : unmutable(unchangeble) and we use curved bracket
gender = ("male", " female", " others")
print(gender)
# gender[0] = "male2"  # Cannot modify tuples - they are immutable
print(len(gender))
print(gender[1])
print(gender[2])
print(gender[1:2])
print(gender[0:3])


#tuple concatination
tuple1 = (1,2,3)
tuple2 = (10,20,30)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

#tuple repetation
repeated_tuple = (1234,99,"nagaraj")*100
print(repeated_tuple)