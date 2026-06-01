# Converted from notebook: ifStatements.ipynb

# # Basic If Statements
cities = ["laramie","casper","jackson","cheyenne"]

for city in cities:
    if city == "laramie":
        print(city.upper())
    else:
        print(city.title())

# The previous cell does the following:
# * declares the list `cities = ["laramie","casper","jackson","cheyenne"]`
# * Iterates through each element 
# * Checks `if city == "laramie":` 
#     * Which is checking to see if the variable `city` holds the value `laramie` for a given iteration
#         * If yes that value is printed in all caps
#     * Otherwise the value is printed in title case
# # Boolean expressions and checks
city = "Laramie"
print(city=="Laramie")

# The previous cell is a simple comparison
# WE assign the value of `Laramie` to the variable `city`
# WE then use the equality check `==`
city = "Laramie"
print(city=="Cheyenne")
print(city=="laramie")

city = 'Laramie'
print(city.upper()=='laramie'.upper())

city = "Laramie"
city_two = "Cheyenne"

print(city == city_two)
if city == city_two:
    print(f"{city} is equal to {city_two}")

print(city != city_two)
if city != city_two:
    print(f"{city} is not equal to {city_two}")

print("dog"!="dog")
print("dog"!="cat")

age_to_drive = 16

print(age_to_drive == 16)
print(age_to_drive == 15)

age_to_drive = 16

print(age_to_drive != 16)
print(age_to_drive != 15)

age_to_drive = 16
print(age_to_drive < 16)
print(age_to_drive > 16)
print(age_to_drive <= 16)
print(age_to_drive >= 16)

age_zero = 22
age_one = 20 
print(age_zero >= 21)
print(age_one >= 21)
print(age_zero >= 21 and age_one >= 21)
print((age_zero >= 21) and (age_one >= 21))

age_zero = 22
age_one = 20 
print(age_zero >= 21)
print(age_one >= 21)
print(age_zero >= 21 or age_one >= 21)

# ## Boolean expression practice
# ### Evaluating the Booleans 
# In the code cell below create **4** print statements using an `and` to get the output from the following combinations 
# * false and false
# * false and true
# * true and false
# * true and true  
#
#
# You can have these expressions in the print statement, an example output would be:   
# `For false and false the output  is: false`   
# With an example print statement of:   
# ```python
# print(f"For false and false the output is: {False and False}")
# ```


# ### Repeat the above, but now using `or` rather than `and`


# # `in` Checks
#check to see if Laramie is in the list
cities = ["Laramie","Casper","Jackson Hole","Cheyenne"]

if "Laramie" in cities:
    print("Laramie already in the list")

cities = ["Laramie","Casper","Jackson Hole","Cheyenne"]
#see if there is a space in the first element in the list
if " " in cities[0]:
    print(f"There is a space in {cities[0]}")
#see if there is a space in the third element
if " " in cities[2]:
    print(f"There is a space in {cities[2]}")

#First declare a list of banned phrases
banned_phrases = ["Go Rams","Boise is a state"]
#Check to see if the phrase "Go Pokes" is in that list
if "Go Pokes" not in banned_phrases:
    print("Go Pokes")

# ### `in`-check practice 
# Given the list below, print all states with a space in their name
#
#
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# # `if` evaluations
#Some basic if statements
#Done only using the boolean operators True and False
if True:
    print('This will print')

if False:
    print('This not will print')

if not True:
    print('This not will print')

if not False:
    print('This will print')

#Assigns the integer value  of 16 to the variable age
age = 19 

#checks to see if the value referenced by age is greater than or equal to 18 
if age >= 18:
    print("you can vote!")

# # `if-elif-else` chaining
#first sets age to be 17
age = 17
#adds in an else statement which will execute when if if statement evaluates to false
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You can't yet vote")

#Now adds in an elif
#Remember, only one of these cases can execute

age = 12 
if age < 4:
    price = 2
elif age < 65:
    price = 12
else:
    price = 7

print(f"Your cost of admission is ${price}.00")

#This one adds in an extra elif, still only one may execute
age = 12 
if age < 4:
    price = 2
elif age < 18:
    price = 10
elif age < 65:
    price = 12
else:
    price = 7

print(f"Your cost of admission is ${price}.00")

# This one omits the else, so there is no default case 
age = 12 
if age < 4:
    price = 2
elif age < 18:
    price = 10
elif age < 65:
    price = 12
elif age >= 65:
    price = 7

print(f"Your cost of admission is ${price}.00")

#First declares our city list
cities = ["laramie","casper","jackson","cheyenne"]

#Then checks to see if certain values are held within the list
if 'laramie' in cities:
    print("Laramie is in Wyoming")
if 'cheyenne' in cities:
    print("Cheyenne is in Wyoming")

# # `if` statements in loop
cities = ["Laramie","Casper","Jackson","Cheyenne"]
#now we can iterate through the list and do checks on the specific values
for city in cities:
    if 'a' in city.lower():
        print(f"{city} has an 'a' in it!")

cities = ["Laramie","Casper","Jackson","Cheyenne"]

#checks to see if a value matches something, uses the strong casing method to ensure the casing matches
for city in cities:
    if city.lower() == 'laramie':
        print(f"{city} is the home of the University of Wyoming")

user_home_cities = []

#first checks to see if there are elements in the list, before trying to do something with it
if user_home_cities:
    for city in cities:
        print(city)
else:
    print("No home cities")

user_home_cities = []

if len(user_home_cities) == 0:
    print("No cities stored")
else:
    print(f"There are {len(user_home_cities)} stored")

#This code uses multiple lists
#One is a list of possible toppings for a pizza, the next is the requested toppings
#It goes through and checks if each requested topping is available

avail_toppings = ['pepperoni', 'extra cheese', 'green peppers', 'bacon']

requested_toppings = ['extra cheese', 'green onions', 'pepperoni']

for req_top in requested_toppings:
    if req_top in avail_toppings:
        print(f"Adding {req_top}")
    else:
        print(f"{req_top}  not available")

# ### Loops and ifs practice
# Given the list of grades below, print what letter grade each grade receives
# * 90-100 **A**
# * 80-89  **B**
# * 70-79  **C**
# * 60-69  **D**
# * <59    **F**
#
# Example output:
# `73 is a C`
grades = [5, 88, 94, 23, 16, 85, 87, 48, 1, 46, 67, 46, 7, 88, 79, 42, 31, 91, 3, 42]

#We can safely check if a list has elements before trying to access the first element,

#Or if a list has an appropriate number before trying to access a certain index

