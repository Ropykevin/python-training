# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

# stars=""
# number=int(input('enter the number: '))
# count=0
# for i in range(number):
#     stars+="*"
#     count+=1
#     print(stars)
    
#     if count==number:
#         print(stars+("."*number))
stars = int(input("enter the number: "))
count =0
for i in range(stars+1):
    value="*"*i
    count+=1
    if count==stars:
        value += ("."*i)
    print(value)

    