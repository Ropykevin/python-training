# marks=int(input("Enter marks: "))

# if (marks>=60):
#     print("A")
# elif(marks>=50):
#     print("B")
# elif(marks>=40):
#     print("C")
# else:
#     print("fail")


# average_marks=int(input("Enter marks"))

# if(average_marks>=70):
#     print("A")
# elif(average_marks>=60)and(average_marks<70):
#     print("B")
# elif(average_marks>=50)and(average_marks<60):
#     print("C")
# elif(average_marks>=40)and(average_marks<50):
#     print("D")
# else:
#     print("E")


# number= int(input("Enter mnumber: "))
# if(number%2==0):
#     print("even")
# else:
#     print("ODD")

# num1= int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if(num1>num2 and num1>num3):
#     print(f"{num1} is the largest")
# elif(num2>num1 and num2 >num3):
#     print(f"{num2} is the largest")
# else:
#     print(f"{num3} is the largest")

# temperature= float(input("enter temperature: "))
# if (temperature > 30):
#     print("Temp is too high")
# elif(temperature<15.5):
#     print("low temperature")
# else:
#     print("Normal temp")

# add a condition that checks if the temperature is below 15.5
# print the temperature is too low

temperature = int(input("enter temperature in degree ceilcius: "))
if (temperature > 100):
    valid=("extreme temperature")
elif (temperature > 30 and temperature < 100):
    valid=("temperature is too high")
elif (temperature <= 30 and temperature > 15.5):
    valid=("normal temperature")
elif (temperature < 15.5):
    valid=("low temperature")
else:
    valid=("enter valid temperature")

print(valid)
