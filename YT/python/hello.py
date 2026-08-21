name = "farhan"
string = f"hi there , my name is {name}"
print(string)

#string methods
s1 = string.replace("hi", "hey")
print(s1)

temperature = 25
if temperature > 30:
    print("its hot outside")
else:
    print("good to go!")
    


age = 17
licence = True
if age >=18 and licence:
    print("you can drive")
else:
    print("you cannot drive")
    
for i in range(5):
    print(i)

my_list = ["alice",25,True]

person = {
    "name" : "Alice",
    "age" : 25,
    "city" : "New york"
}

person["age"]
person["name"]
person["license"] = True
del person["license"]