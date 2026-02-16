# ███▓▒░  Day 4: Py30 Exercises  ░▒▓███
"""
TODO — Day 4 Exercises Overview

[x] Exercise 01 : Concatenate 'Thirty', 'Days', 'Of', 'Python'
[x] Exercise 02 : Concatenate 'Coding', 'For', 'All'
[x] Exercise 03 : Declare company variable
[x] Exercise 04 : Print company variable
[x] Exercise 05 : Print length of company string
[x] Exercise 06 : Change characters to uppercase
[x] Exercise 07 : Change characters to lowercase
[x] Exercise 08 : Use capitalize(), title(), swapcase()
[x] Exercise 09 : Slice out the first word
[x] Exercise 10 : Check for 'Coding' in string
[x] Exercise 11 : Replace 'Coding' with 'Python'
[x] Exercise 12 : Change 'Python for Everyone' to 'Python for All'
[x] Exercise 13 : Split string using space separator
[x] Exercise 14 : Split string at the comma
[x] Exercise 15 : Character at index 0
[x] Exercise 16 : Last index of string
[x] Exercise 17 : Character at index 10
[x] Exercise 18 : Create acronym for 'Python For Everyone'
[x] Exercise 19 : Create acronym for 'Coding For All'
[x] Exercise 20 : Position of first 'C'
[x] Exercise 21 : Position of first 'F'
[x] Exercise 22 : Last occurrence of 'l'
[x] Exercise 23 : First occurrence of 'because'
[x] Exercise 24 : Last occurrence of 'because'
[x] Exercise 25 : Slice out 'because because because'
[x] Exercise 26 : Find position of 'because'
[x] Exercise 27 : Slice out 'because because because' (redundant check)
[x] Exercise 28 : Check if starts with 'Coding'
[x] Exercise 29 : Check if ends with 'coding'
[x] Exercise 30 : Remove trailing spaces
[x] Exercise 31 : Check isidentifier()
[x] Exercise 32 : Join list with hash
[x] Exercise 33 : New line escape sequence
[x] Exercise 34 : Tab escape sequence
[x] Exercise 35 : Circle area formatting
[x] Exercise 36 : Arithmetic formatting
"""

# # Exercise 01
#   - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Logging Sentence glued
print(" ".join(['Thirty', 'Days', 'Of', 'Python']))

# # Exercise 02
#   - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : List of words
CFA = "Coding For All"
CFA_LIST = CFA.split(" ")

print(" ".join(CFA_LIST))

# # Exercise 03 - 11
#   - 03. Declare a variable named company and assign it to an initial value "Coding For All".
#   - 04. Print the variable company using print().
#   - 05. Print the length of the company string using len() method and print().
#   - 06. Change all the characters to uppercase letters using upper() method.
#   - 07. Change all the characters to lowercase letters using lower() method.
#   - 08. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
#   - 09. Cut(slice) out the first word of Coding For All string.
#   - 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
#   - 11. Replace the word coding in the string 'Coding For All' to Python.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Logging : Initiated Variable
print(CFA)
print(f"\t   5. The Length: {len(CFA)}")
print(f"\t   6. Upper Case: {CFA.upper()}")
print(f"\t   7. Lower Case: {CFA.lower()}")
print(f"\t 8.1. First Word is Capitalized: {CFA.capitalize()}")
print(f"\t 8.2. First Letter of every Word Capitalized: {CFA.title()}")
print(f"\t 8.3. Lower and Upper cases switch places: {CFA.swapcase()}")
print(f"\t   9. First word: \"{CFA[0:6]}\"")
print(f"\t  10. Does {CFA} contain the word \'Coding\'? {CFA[0:6] == 'Coding'}, \n\t\tThen where does it start? at the number {CFA.find('Coding') + 1} Character")
print(f"\t  11. It's time for a big change from now on {CFA.replace('Coding', 'Python')}")

# # Exercise 12
#   - Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

PFE = 'Python For Everyone'
PFE_LIST = PFE.split(" ")

print(PFE.replace("Everyone", "All"))

# # Exercise 13
#   - Split the string 'Coding For All' using space as the separator (split()) .
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Logging : Initiated Variable again
print(f"{CFA.split(' ')}")

# # Exercise 14
#   - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(f"{'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(',')}")

# # Exercise 15 - 17
#   - 15. What is the character at index 0 in the string Coding For All.
#   - 16. What is the last index of the string Coding For All.
#   - 17. What character is at index 10 in "Coding For All" string.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(f"Index [0] of {CFA} is {CFA[0]}")
print(f"Last Index of {CFA} is {CFA[-1]}")
print(f"Index [10] of {CFA} is \"{CFA[10]}\"")

# # Exercise 18
#   - Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(f"{''.join((PFE_LIST[0][0], PFE_LIST[1][0], PFE_LIST[2][0]))}")

# # Exercise 19 - 21
#   - 19. Create an acronym or an abbreviation for the name 'Coding For All'.
#   - 20. Use index to determine the position of the first occurrence of C in Coding For All.
#   - 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(f"{''.join((CFA_LIST[0][0], CFA_LIST[1][0], CFA_LIST[2][0]))}")
print(f"The first occurrence of C in {CFA} is at {CFA.index('C')}")
print(f"The first occurrence of F in {CFA} is at {CFA.index('F')}")

# # Exercise 22
#   - Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(f"last occurrence of l in {(CFA + ' People')} is at {(CFA + ' People').rfind('l')}")

# # Exercise 23 - 27
#   - 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#   - 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#   - 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#   - 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#   - 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

Grammar = 'You cannot end a sentence with because because because is a conjunction'

print(Grammar.index("because")) # both 23 and 27
print(Grammar.rindex("because"))
print(Grammar[Grammar.index("because"):Grammar.rfind("because")+len("because")])

# # Exercise 28 - 30
#   - 28. Does 'Coding For All' start with a substring Coding?
#   - 29. Does 'Coding For All' end with a substring coding?
#   - 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(CFA.index("Coding") == 0)
print((CFA.split(" ")[-1]) == "Coding")
print('   Coding For All      '.strip(" "))

# # Exercise 31
#   - 31. Which one of the following variables return True when we use the method isidentifier():
#      - 30DaysOfPython
#      - thirty_days_of_python
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

Course = ["30DaysOfPython", "thirty_days_of_python"]
Status = {True: "Right", False: "Wrong"}

print(f'Variable name "{Course[0]}" is the {Status[Course[0].isidentifier()]} way of naming a variable')
print(f'Variable name "{Course[1]}" is the {Status[Course[1].isidentifier()]} way of naming a variable')

# # Exercise 32
#   - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print(" # ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# # Exercise 33
#   - Use the new line escape sequence to separate the following sentences.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print("I am enjoying this challenge.\nI just wonder what is next.")

# # Exercise 34
#   - Use a tab escape sequence to write the following lines.
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print("""
Name\t\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki
""")

# # Exercise 35
#   - Use the string formatting method to display the following:
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print("radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.")

# # Exercise 36
#   - Make the following using string formatting methods:
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

print("""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
""")