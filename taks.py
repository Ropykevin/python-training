trainees = ["John", [2, ["James", "Mary"]]]
trainees[1][1].remove("Mary")
trainees.remove("John")


# Using a method add 56 at the end of the list.
trainees = ["John", [2, ["James","Mary"]]]
trainees[1][1].insert(1,"mike")
trainees[1].insert(2,56)
trainees[1][0]=8
print(trainees)
