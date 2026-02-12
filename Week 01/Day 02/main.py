# TODO — Day 2 Sections Overview
# [x] Section A.1 — Collect basic user information
# [x] Section A.2 — Boolean variable declarations
# [x] Section A.3 — Multiple variable assignment on one line
# [x] Section B.1 — Type checking using type()
# [x] Section B.2 — Length check using len()
# [x] Section B.3 — Compare first and last name lengths
# [x] Section C.1 — Arithmetic operations and calculations
# [x] Section D — Circle area and circumference calculations

# Day 2: Py30 Challenge
import math

# Section A.1:
first_name = input("First Name: ")
last_name = input("Last Name: ")
full_name = first_name + last_name
country = input("Country: ")
city = input("City: ")
age = int(input("Age: "))
year = int(input("Year: "))

# Section A.2:
is_married = False
is_true = True
is_light_on = False

# Section A.3:
Car, Model, Year = "Toyota", "Corolla", 2026

# Section B.1:

# Types of Section A.1 and A.2:
Holder = type(first_name)
print("Type is:", Holder)

Holder = type(last_name)
print("Type is:", Holder)

Holder = type(full_name)
print("Type is:", Holder)

Holder = type(country)
print("Type is:", Holder)

Holder = type(city)
print("Type is:", Holder)

Holder = type(age)
print("Type is:", Holder)

Holder = type(year)
print("Type is:", Holder)

Holder = type(is_married)
print("Type is:", Holder)

Holder = type(is_true)
print("Type is:", Holder)

Holder = type(is_light_on)
print("Type is:", Holder)

# Section B.2:
len(last_name)

# Section B.3:
if len(first_name) < len(last_name):
    print("First name is shorter")
elif len(first_name) == len(last_name):
    print("First and Last name's lengh is equal")
else:
    print("Last name is shorter")

# Section C.1:
Num_01 = int(input("Please enter a number (1): "))
Num_02 = int(input("Please enter a number (2): "))

total = Num_01 + Num_02
diff = Num_01 - Num_02
product = Num_01 * Num_02
division = Num_01 / Num_02
remainder = Num_01 // Num_02
exp = Num_01**Num_02
floor_division = int(division)

print(
    "Total: ",
    total,
    "| Diff: ",
    diff,
    "| Product: ",
    product,
    "| Div: ",
    division,
    "| Remainder: ",
    remainder,
    "| Exp: ",
    exp,
    "| Floor Div: ",
    floor_division,
)

# Section D:
radius = int(input("Give me a circle radius: "))
pi = math.pi

area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

print("A = πr² = π·", radius, "² ≈", area_of_circle)
print("C = 2πr = 2·π·", radius, "≈", circum_of_circle)
