# Write a program that displays a numbers 1 to 50 inside a list.

# From 1 above display the ones divisible by 7 and 5 inside a list.

# Find sum and average of values in the range between 10 to 40.

# Put in a list the first 10 odd numbers between 10 to 50. 

# 1
numbers=[]
for i in range(1,51):
    numbers.append(i)
print(numbers)

# From 1 above display the ones divisible by 7 and 5 inside a list

digits=[]
for i in range(51):
    if (i%7==0) or (i%5==0):
        digits.append(i)
print(f"{digits} digits")

# for i in range(1,51):
#     numbers.append(i)

# for y in numbers:
#     print(y)

# 3 Find sum and average of values in the range between 10 to 40.
values=[]
for i in range(10,41):
    values.append(i)

print(values)

sumation=sum(values)

average=sumation/len(values)
print(f"{sumation} sum")
print(f"{average} average")


# 4 Put in a list the first 10 odd numbers between 10 to 50.

main=[]
for i in range(10,51):
    if (i%2!=0):
        main.append(i)
        if len(main)==10:
            break
print(f"{main} main")