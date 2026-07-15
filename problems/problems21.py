#problem : 21 Question 1..
#1.Tuple print ಮಾಡು.
#2.Length print ಮಾಡು.
#3.ಮೊದಲ element print ಮಾಡು.
#4.ಕೊನೆಯ element print ಮಾಡು.
#5.Tuple ನಲ್ಲಿ 50 ಇದೆಯಾ ಇಲ್ಲವಾ check

tup = (10, 20, 30, 40, 50)
print(tup)
print(len(tup))
print(tup[0])
print(tup[4])
if 50 in tup:
    print("50 found")
else:
    print('50 not found')

##questin 2..
#1.ಎಲ್ಲಾ elements print ಮಾಡು.
#2.Sum ಕಂಡುಹಿಡಿ.
#3.Maximum number print ಮಾಡು.
#4.Minimum number print ಮಾಡು.

marks = (78, 92, 65, 88, 95)
print(marks)
print(sum(marks))
print(max(marks))
print(min(marks))

## questin 3...
#1.Duplicate remove ಮಾಡು.
#2.Ascending order ನಲ್ಲಿ sort ಮಾಡು.
#3.ಮತ್ತೆ tuple ಆಗಿ convert ಮಾಡಿ print ಮಾಡು.

numbers = (5, 2, 8, 5, 1, 2, 9)
unique = set(numbers)
sorted_numbers = sorted(unique)
print("original tuples", numbers)
print("after removing duplicates", unique)
result = tuple(sorted_numbers)
print("result as tuple:", result)


