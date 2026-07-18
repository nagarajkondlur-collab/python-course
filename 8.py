#TOPIC : IF, ELSE , ELIF AND CONDITIONAL STATEMENT 
x = 24
# yanadru 
if x %2 ==0:
    print("x is even") # anta print madu
else : # ella andre
    print("x is odd")
    
x = 99
# yanadru 
if x %2 ==0:
    print("x is even") # anta print madu
else : # ella andre
    print("x is odd")
     
signal = "red"
if signal =="red":
    print("STOP")
elif signal == "yellow": # ELIF USED TO CHECK SO MANY YANDRU
    print("READY")
elif signal =="green":
    print("GO")
else:
    print("signal is off")
    
time = 3567

 
if time ==8:
    print("time for breakfast")
elif time ==1:
    print("time for lunch")
elif time ==6:
    print("time for snacks")
elif time ==9:
    print("time for dinner")
elif time ==12:
    print(" time for sleep")

else:
    print("no time is alloted for meal ")       
    
 # with logical operators
att = 75 
is_teacher_friend = True
if att >= 75 and is_teacher_friend:
    print("able to attend exam") ## ATTENDENCE> 75 MATTE TEACHER FRIEND 
    # agidre matra exam ella no exam avag and logic use madthivi
else:
    print("NO EXAM")

att = 45
is_teacher_friend = True
if att >= 75 and is_teacher_friend:
    print("able to attend exam") 
else:
    print("NO EXAM")
    
att = 99
is_teacher_friend = False
if att >= 75 or is_teacher_friend:
    print("able to attend exam") 
else:
    print("NO EXAM") ## attendence > 75 edru agutte athva teacher
# friend agidru agutte yavd adhru ondh agirlay beku avag exam allow

## if else olgade ennondh if else use mado concept
gender = input("gender>")
age = int(input("age>"))
if gender =="female":
    print("free bus ticket")
else:# adh bittu bere evishtralli
    if age < 12:
        print("half ticket")
    elif age> 60:
        print("discount offer")
    elif age <5:
        print("free ticket")
    else:
        print("pay full fees")
        