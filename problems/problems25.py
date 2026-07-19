# PROBLEM : 25 - IF,ELIF ,ELSE PRACTICE

# 1.SMART LOGIN SYSTEM
username = input("Username = ")
password = int(input("Password = "))

if username == "nagaraj" and password == 6361273988:
    print("Login Successful")
                                         ## edhuk equal ella andree
elif username == "nagaraj" and password != 6361273988:
    print("Wrong Password") ## passsword not equal to ella ande ee symol use madbeku !=

elif username != "nagaraj" and password == 6361273988:
    print("Wrong Username") ## username not equal to ella ande ee symol use madbeku !=

else:
    print("Invalid Username and Password")