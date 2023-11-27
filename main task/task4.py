# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email=input("enter email: ")
if "@" and "." in email:
    print("valid email")
else:
    print("invalid email")