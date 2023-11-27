days = ("monday", "tuesday","wednesday","thursday", "friday","saturday","sunday")
# 2. Using a function a find the length of the tuple.
print(len(days))
# Replace Thursday with Thur
days = ("monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday")
days=list(days)
days[3]="Thur"
print(days)
days=tuple(days)
print(days)