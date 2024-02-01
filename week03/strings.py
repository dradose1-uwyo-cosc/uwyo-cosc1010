# Danny Radosevich
# COSC 1010
# Week Three 
# Strings

a = "this is a string"
b = 'so is this' 
c = "when they hear that he's 'a-comin'"
d = 'And then I said "Python is fun!"'


#changing case 
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#Variables in strings 
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello There, {full_name.title()}")

#white space
print("python")
print("\tpython")

print("--------------")
print("pythonpython")
print("python\npython")
print("--------------")
print("python\n\tpython")

#Stripping whitespace 
string_one = "py    "
string_two = "thon"

print(f"{string_one}{string_two}")
print(f"{string_one.rstrip()}{string_two}")

#Removing prefixes 
wyoweb = "https://wyoweb.uwyo.edu/"
print(wyoweb)

print(wyoweb.removeprefix("https://"))

#Syntax errors
#print('cause the western folks all know, he's a high-falootin', rootin, tootin', '`) #uncomment this line to get the error
print("cause the western folks all know, he's a high-falootin', rootin, tootin',") #this is correct 