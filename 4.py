# operators 1
a = 10
b = 20
a = a + b
print(a)
# instead of a =a+b we can put a +=b ,shown below
a = 25
b = 10
a += b
print(a)
a = 10
b = 100
a *= b
print(a)

# operators-comparision
a = 20
b = 30
print(a==b) # to  check a and b are equal or not
print(a != b) # this is used to check variables are not equal
print(a>b)
print(a<b)
print(a<10)
print(a<=25)
print(a>=25)


#  operators-logical operators
print(1>2 and 2>1) ## here when and is used it applies on both means it check both operation ,2 also bosses
print(1>2 or 2>1) ## here it applys on only one opertion , if one is true then whole code is true

# operators- membership operators
s = " microsoft"
print("m" in s) ## to tell presence and absence of letter
print("z" in s)
s2 = "amazon"
print(("m" in s) and ("i" in s2))
print(("t" in s) and ("a" in s2))
print(("m" in s) or ("k" in s2))
print(not("k" in s))

