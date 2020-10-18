#User input
sc= input("Please enter the score (A number between 0.0 and 1.0): ")
try:
    sco=float(sc)
except:
    print("Wrong input, please try again")
    quit()
#Establishing a corresponding grade based on the entered score
if sco>=0.9:
    if sco <=1.0:
        print("Congratulations! you got an A")
    else:
        print("Wrong score, please try again")
elif sco>=0.8:
    print("Good work! you got a B")
elif sco>=0.7:
    print("Not so bad. You got a C")
elif sco>=0.6:
    print("You can do it better. Your grade is D")
else:
    if sco>=0:
        print ("What happened? Your grade is F")
    else:
        print("Wrong score, please try again")
