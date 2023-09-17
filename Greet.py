import time
a= time.localtime()
b=input("Hello Mate!! How can I be of assistance to you today?\n May I kindly ask for your name :")  
h=a.tm_hour
m=a.tm_min
S=a.tm_sec
print("Time is-" ,f"{h}:{m}:{S}")
if(4<=h<12 ):
    print("Good morning!", b)
elif(16>=h>=12):
    print("Good Afternoon!",b)  
else:
    print("Good night!",b)      

