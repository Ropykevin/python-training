# # Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
# # name = “  JOHn  .“ to “john”
# name="  JOHn  ."
# name=name.lower() .replace("."," ").strip()
# # name=name.strip(" .").lower()
# print(name)

# # Slice the below string to get you the resulting sentence:
# # sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# # sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
# sentence_one="The Dog Breed is German Shepherd"
# # print(sentence_one[8:23])
# # sentece_two=slice(8,23)
# # print(sentence_one[sentece_two])

# sentence2 = 'Defeats for the Clinton forces ,this was her moment of triumph'
# print(sentence2[16:30])

# # Split the below sentence using a semicolon i.e ; And display length of the result. 
# # “The lazy dog; ran so fast; it hit the wall.” 

# records= "The lazy dog; ran so fast; it hit the wall."
# split_records=records.split(";")
# print(len(split_records))

# # first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
# first_name = "  Joh.n"
# last_name = "   Do,e"
# first_name=first_name.strip().replace(".","")
# last_name=last_name.strip().replace(",","")
# full_name= first_name + " " + last_name
# print(full_name)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r = '["E","W","C"]'
# r2=''.join(r)
r2 = ''.join(filter(str.isalpha, r))
print(r2)


sentence2 = 'Defeats for the Clinton forces ,this was her moment of triumph'
print(sentence2.index("e",16))
