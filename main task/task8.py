# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, 
# for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
speed = int(input( "enter speed: "))

speed_limit=70
demerit_points=0
if speed <= speed_limit:
    print("ok")
elif(speed>speed_limit and speed<75):
    demerit_points=1
else:
    demerit_points=round((speed-speed_limit)/5)
    if demerit_points>12:
        print("license suspended ")
    else:
        print(f"demerit points: {demerit_points}")

print(demerit_points)