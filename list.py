person=["abigail murungi",18,"female","Nairobi","07777777"]
print(person[-1])

days_week=["sunday","monday","tuesday","wenesday","thusday","friday","satuday"]
print(days_week.index("wenesday"))
print(days_week[3])

group_list=[[1,2,3,4,5],"monday","tuesday"]
print(group_list[1][-1])
print(len(group_list))

add_list= days_week + group_list
print(add_list)

print("friday"  not in group_list)
# print(group_list.index("friday"))

group_list = [[1, 2, 3, 4, 5], "monday", "tuesday"]
group_list[-1]="friday"
del group_list[-1]
print(group_list)

group_list = [[1, 2, 3, 4, 5], "monday", "tuesday", "tuesday"]

group_list.append("friday")
print(group_list)
# group_list.sort()
print(group_list)

trainees = ["John", [2, ["James", "Mary"]]]
print(trainees[1][1][0])




