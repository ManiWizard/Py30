# # ███▓▒░  Day 4: Py30 Training  ░▒▓███

# # Training 00 
#  - Length of an Variable
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variable and Value
Lipsum = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# Logging : The Length of Lipsum
print(len(Lipsum))

# # Training 01
#   - Multiline Comments and Strings
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring Variable and Value
Message = """ But this is a value for the variable message
That can span across multiple lines."""

# Logging
print(Message)

# # Training 02 
#   - String Concatenation
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring Variables and Values
Forename = "Mani "
Surname = "Mahmoudi"

# Operations:
# Concatenating Forename and Surname
Name = Forename + Surname

# Logging 
print(Name)

# # Training 03
# - Escape Sequences
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring Variables and Values 
Sentence = "Py30: 30 Days Python Challenge \n\t☑️ Day 01 : Completed\n\t☑️ Day 02 : Completed\n\t☑️ Day 03 : Completed\n"
Path     = "C:\\Python\\"

# Logging 
print(Sentence)
print(f"Project name is \'Py30\' and the path to is {Path}")

# # Training 04
#  - F-String f""
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring Variables and Values
Language = "Python"
Level     = 4

# Logging:
# Gluing texts using F-string
print(f"Proficiency in {Language} is level {Level}.")

# # Training 05 
#  - index of a string
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring Variables and Values (Already done before)
# Language = "Python"

# Logging index of a String Value
print(f"First letter of the word \'{Language}\' is \'{Language[0]}\'")
print(f"Last letter of the word \'{Language}\' is \'{Language[-1]}\'")

# # Training 06
#  - Slicing Strings
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring Variables and Values
Blog = "Blog post: Conspiracy Theory \nAs we know Python is a bad language that is created to make Programmers lazy, \nand because it didn't work big corporations had to make AIs to make Programmers Dumb instead of lazy.\n"
Course = "Thirty Days"

# Logging : A Slice of the Value of Language Variable
print(Blog)
print(f"Noted: {Blog[30:106]} \n")
print(f"{Course[0:6:2]}")
print(f"{Course[::-1]}")

# # Training 07
#  - String Methods
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variables and Values
Country = "North Korea"
Leader  = "Kim Jung Un"
Status = f"The current leader of {Country.upper()} is Kim Jong-il"

# Logging Status of the country
print(Status.replace("Kim Jong-il", Leader))

# # Training 08
#  - Splitting Strings
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variable and Vlues
Tech_Stack = "Python, HTML, CSS, React"

# Logging : Tech Stack
print(Tech_Stack.split(", "))

# # Training 09
#  - Searching Strings
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variable and Value
Challenge = "Thirty Days of Python by Asabeneh"

# Logging : Checking if the Challenge is by Asabeneh
print(Challenge.find("Asabeneh"))

# # Training 10
#  - Counting Occurrences
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variable and Value
# Challenge = "Thirty Days of Python by Asabeneh" # Already done

#Logging : How many times letter y appears in the sentence
print(Challenge.count("y"))


# # Training 11
#  - Joining Lists
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variable and Values
Libraries = ['Django', 'Flask', 'NumPy', 'Pandas']

# Logging : Joining the list items
print(" | ".join(Libraries))

# # Training 12
#  - Formatting
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : Variables and Values
Lang = "Python"
Version = 3

# Logging : My hatred for Python
print("I hate %s specially version %d" %(Lang, Version))