# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254…
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

phone_number = input("Enter phone number: ")
# +254
if (phone_number[0:4] == "+254" and len(phone_number) == 13):
    valid = (f"Valid phone number {phone_number}")
    print(valid)
    # 07 and 01
elif ((phone_number[0:2] == "07" and len(phone_number) == 10) or
       (phone_number[0:2] == "01" and len(phone_number) == 10)):
    new_p = ("+254" + phone_number[1:])
    valid = f"{new_p} is valid"
    print(valid)
elif((phone_number[0:1]=='7'and len(phone_number)==9)or
      (phone_number[0:1]=='1'and len(phone_number)==9)):
    new_p="+254" + phone_number
    valid= f"{new_p} is valid"
    print(valid)
elif(phone_number[0:3]=="254" and len(phone_number)==12):
    new_p= "+" + phone_number
    valid = f"{new_p} is valid"
    print(valid)
else:
    print("invalid number")

