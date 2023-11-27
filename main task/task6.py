# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password="admin@123"
attempts=0
while attempts<4:
    password = input("enter vpassword: ")
    if password==correct_password:
        print("access granted")
        break
    else:
        print("incorect password")
        attempts+=1
        if attempts==4:
            print("account blocked")

# for i in range(attempts):
#     password = input("enter vpassword: ")
#     if password==correct_password:
#         print(" access granted")
#         break  
#     else:
#         attempts += 1
#         if attempts<4:
#             print(" wrong password"+attempts-i-1)
#         else:
#             print("account blocked")

# whi

# while attempts>0:
    # if password==correct_password:
    #     print("access granted")
    #     break
    # elif attempts:

