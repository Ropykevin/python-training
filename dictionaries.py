# creating  dictionaries
person = {"name": "Ropy kevin",
     "age": 60,
     "location": "Nairobi",
     "email": "ropykevin@gmail.com"}

# accessing values in a dictionary(use keys )
print(person["age"])
print(person["location"])
print(person["name"])

# updating values in a dictionary

person["age"]=20
person["email"]="kevin@gmail.com"
person["location"]='mombasa'
person["name"]="kevin"
print(person)

# adding a new key value pair
person["gender"]="Male"
person["adress"]="518-00100"

# dictionary methods

print(person.get("age"))

new_data={"course":"education","campus":"nairobi"}

person.update(new_data)
person.pop("age")
print(person)

print(person.copy())
print(person.popitem())
# print(person.items())

# print(len(person))


