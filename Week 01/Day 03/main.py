# TODO — Day 3 Exercises Overview
# [x] Exercise 1 — Declare age as integer variable
# [x] Exercise 2 — Declare height as float variable
# [x] Exercise 3 — Declare a complex number variable
# [x] Exercise 4 — Triangle area calculation (0.5 * base * height)
# [x] Exercise 5 — Triangle perimeter calculation (a + b + c)
# [x] Exercise 6 — Rectangle area and perimeter
# [x] Exercise 7 — Circle area and circumference
# [x] Exercise 8 — Slope, x-intercept, and y-intercept of y = 2x - 2
# [x] Exercise 9 — Slope and Euclidean distance between two points
# [x] Exercise 10 — Compare slopes
# [x] Exercise 11 — Quadratic evaluation (x^2 + 6x + 9)
# [x] Exercise 12 — Length comparison ('python' vs 'dragon')
# [x] Exercise 13 — Logical 'and' operator check ('on' in both words)
# [x] Exercise 14 — 'in' operator check ('jargon' in sentence)
# [x] Exercise 15 — Logical 'not' operator check
# [x] Exercise 16 — Convert length to float and string
# [x] Exercise 17 — Even number check using modulo
# [x] Exercise 18 — Floor division vs int conversion comparison
# [x] Exercise 19 — Type comparison ('10' vs 10)
# [x] Exercise 20 — int('9.8') comparison
# [x] Exercise 21 — Pay calculator (hours × rate × days)
# [x] Exercise 22 — Years to seconds calculation
# [x] Exercise 23 — Power table display

# ███▓▒░  Day 3: Py30 Exercises  ░▒▓███
import math

# Day 3 Playground

print("                [=- Arithmetic operations -=]")

# Variables and their values organized on top
Num_A = 3
Num_B = 7
Num_C = 15

# Arithmetic operations
AO_Total            = Num_A + Num_B
AO_Diff             = Num_B - Num_C
AO_Product          = Num_A * Num_C
AO_Division         = Num_A / Num_B
AO_Remainder        = Num_A % Num_C
AO_Floor_Division   = Num_B // Num_C
AO_Exponential      = Num_C ** Num_B

print("==============================================================")
print("| We got 3 numbers that will do Arithmetic operations on 'em |")
print("|                   A = 3 | B = 7 | C = 15|                  |")
print("==============================================================")
print("                   Total | (A + B)  | ", AO_Total)
print("              Difference | (B - C)  | ", AO_Diff)
print("                 Product | (A * C)  | ", AO_Product)
print("                Division | (A / B)  | ", AO_Division)
print("               Remainder | (A % C)  | ", AO_Remainder)
print("          Floor Division | (B // C) | ", AO_Floor_Division)
print("             Exponential | (C ** B) | ", AO_Exponential)
print("==============================================================")
print("")

# Exercises day 3

# 1. Declare your age as integer variable
# 2. Declare your height as a float variable
# 3. Declare a variable that store a complex number
Age = 23
Height = 1.75
Complex_Number = 2 + 3j

print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 4. Triangle area (area = 0.5 x b x h)
Triangle_Base = float(input("Please enter the base of the Triangle: "))
Triangle_height = float(input("Please enter the height of the Triangle: "))
Triangle_Area = 0.5 * Triangle_Base * Triangle_height
print("The area of the Triangle is: ", Triangle_Area)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 5. Triangle perimeter (perimeter = a + b + c)
Triangle_side_A = float(input("Enter side A of the Triangle: "))
Triangle_side_B = float(input("Enter side B of the Triangle: "))
Triangle_side_C = float(input("Enter side C of the Triangle: "))
Triangle_Perimeter = Triangle_side_A + Triangle_side_B + Triangle_side_C
print("The perimeter of the Triangle is: ", Triangle_Perimeter)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 6. Rectangle area + perimeter
Rectangle_Length = float(input("Please enter the Rectangle's Length: "))
Rectangle_Width = float(input("Please enter the Rectangle's Width: "))
Rectangle_Area      = Rectangle_Length * Rectangle_Width
Rectangle_Perimeter = (Rectangle_Length + Rectangle_Width) * 2
print("Rectangle's Area: ", Rectangle_Area, "| and Perimeter: ", Rectangle_Perimeter)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 7. Circle area + circumference
Circle_Radius = float(input("Please enter the radius of your Circle: "))
PI = math.pi
Circle_Area = PI * Circle_Radius ** 2
Circle_Circumference = 2 * PI * Circle_Radius
print("Area = πr² = π·", Circle_Radius, "² ≈", Circle_Area)
print("Circumference = 2πr = 2·π·", Circle_Radius, "≈", Circle_Circumference)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope = 2
Y_Intercept = -2
X_Intercept = -Y_Intercept / Slope

print("The Slope is:", Slope)
print("The Y-Intercept is:", Y_Intercept)
print("The X-Intercept is:", X_Intercept)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 9. Find the slope and Euclidean distance between point (2, 2) and point (6,10)
P1 = [2, 2]
P2 = [6, 10]

DeltaY = P2[1] - P1[1]
DeltaX = P2[0] - P1[0]

Slope_02 = DeltaY / DeltaX
Distance = math.sqrt((DeltaX ** 2) + (DeltaY ** 2))

print("Slope is: ", Slope_02)
print("Distance is: ", Distance)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 10. Compare the slopes in tasks 8 and 9.
SlopeCompare = Slope == Slope_02
print("Compare value is: ", SlopeCompare)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 11. Calculate y for y = x^2 + 6x + 9. Figure out at what x value y is 0.
X = -3
Y = (X ** 2) + (6 * X) + 9
print('Y is equal to: ', Y)
print("(Hint: y becomes 0 when x is -3)")
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Python = "python"
Dragon = "dragon"
FalsyComp = len(Python) > len(Dragon)
print("Python is longer than Dragon (should be False): ", FalsyComp)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
Part = "on"
On_Both = Part in Python and Part in Dragon
print("is '", Part ,"' on both", Dragon, " and ", Python, ":", On_Both)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 14. Use in operator to check if jargon is in the sentence.
Sentence = "I hope this course is not full of jargon."
Word = "jargon"
IsInSentence = Word in Sentence
print(Sentence)
print("Is jargon a part of the sentence?", IsInSentence)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 15. There is no 'on' in both dragon and python
NotOn_Both = not (Part in Python and Part in Dragon)
print("There is no '", Part ,"' in both", Dragon, " and ", Python, ":", NotOn_Both)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 16. Find the length of the text 'python' and convert to float and then to string
Length_of_Python = len(Python)
ToFloat = float(Length_of_Python)
ToString = str(ToFloat)
print("Length:", Length_of_Python, " Float:", ToFloat, " String:", ToString)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 17. Check if a number is even
Num_01 = 10
isEven = (Num_01 % 2) == 0
print("Is Number ", Num_01, "Even?", isEven)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 18. Check if 7//3 equals int(2.7)
Floor_Division = 7 // 3
intConverted = int(2.7)
isEqual = (Floor_Division == intConverted)
print("Is 7//3 equal to int of 2.7!?", isEqual)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 19. Check if type of '10' equals type of 10
stringTen = type("10")
integerTen = type(10)
Tintin = (stringTen == integerTen)
print("Types equal?", Tintin)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 20. Check if int('9.8') is equal to 10 (convert to float first)
NineEight = int(float('9.8'))
isEqual_02 = (NineEight == 10)
print("int(float('9.8')) == 10 ?", isEqual_02)
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 21. Prompt for hours and rate. Calculate pay.
WorkedHours = float(input("Hours worked per day: "))
WorkedDays = float(input("How many days worked: "))
WagePerHour = float(input("Rate per hour: "))
FinalWage = (WorkedHours * WagePerHour) * WorkedDays
print("You have to pay", FinalWage, "to your Employee.")
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 22. Years -> seconds (assume 100 years max, but user enters actual years)
years_lived = int(input("How many years have you lived? :"))
seconds_lived = years_lived * 31556952
print("You lived ", seconds_lived, "seconds (approx).")
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

# 23. Display the table
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
