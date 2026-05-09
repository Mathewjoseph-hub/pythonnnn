age = int(input("Enter you age"))
if (age>=18):
    print("You are eligible to vote.")
elif (age<18):
    years_left = 18 - age
    print("you are not old enough to vote",years_left)
else:
    print ("you are not eligible to vote")

