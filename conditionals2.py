#if_elif_else
age = int(input("Enter an age :"))

if(age >= 18):
    print("You are eligible to vote ")
elif(age < 0):
    print("You have entered a wrong number")
elif(age == 0):
    print("0 is not a valid age")
else:
    print("you are not eligible to vote")

print("End of program")
