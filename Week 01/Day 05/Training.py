# # ███▓▒░  Day 5: Py30 Training  ░▒▓███

# # Training 00 
#  - Creating a List
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

# Declaring : A list of companies
Companies = ["Epic Games", "Steam", "Activation", "Ubisoft", "FromSoftware"]

# Logging : First and Last Company on the List
print(Companies[0])
print(Companies[-1])

"""
Output:
Epic Games
FromSoftware
"""

# # Training 01
#  - Unpacking and Slicing Lists
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

Fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

Fruits_First, *Fruits_Remaining = Fruits

print(f"The first fruit on the list is {Fruits_First}")
print(f"The remaining fruits on the list are {Fruits_Remaining}")

print(f"Fruits in the middle are {Fruits[1:4]}")

"""
Output:
The first fruit on the list is Apple
The remaining fruits on the list are ['Banana', 'Cherry', 'Date', 'Elderberry']
Fruits in the middle are ['Banana', 'Cherry', 'Date']
"""

# # Training 02
#  - Modifying and Adding items to lists
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

Animals = ['Wolf', 'Leopard', 'Elephant']
Animals[2] = "Lion"

Animals.append("Tiger")
Animals.insert(0, "Bear")

print(f"I Loved {"s, ".join(Animals)}s the most when I was in the zoo.")
print(f"Unfortunately there was {str("Zebra" in Animals).replace("False", "no")} Zebras in the Zoo")

"""
Output:
I Loved Bears, Wolfs, Leopards, Lions, Tigers the most when I was in the zoo.
Unfortunately there was no Zebras in the Zoo
"""

# # Training 03
#  - Remove items, Copy lists, and Join them
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

Tasks = ['Wake up', 'Code', 'Smoke', 'Coffee', 'Sleep', 'Repeat']
Tasks_Backup = Tasks.copy()

Tasks.remove("Smoke")
Last_Task = Tasks.pop() + "ing"

del Tasks[0]

print(f"I usually do some stuff druing a day for example :{", ".join(Tasks)}")
print(f"No wait it seems my tasks are corrupted, \Phew good job I had a Backup of them here you go: \n{", ".join(Tasks_Backup)}")
print(f"I love the last thing I do and it makes me feel great and it's {Last_Task}")

"""
Output:
I usually do some stuff druing a day for example :Code, Coffee, Sleep
No wait it seems my tasks are corrupted, \Phew good job I had a Backup of them here you go:
Wake up, Code, Smoke, Coffee, Sleep, Repeat
I love the last thing I do and it makes me feel great and it's Repeating
"""

# # Training 04
#  - organize and analyze
print("\n◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆\n")

Scores = [88, 56, 92, 78, 56, 99, 88, 56]
Counter = Scores.count(56)
Scores.sort()

del Scores[0]
del Scores[-1]

Index = int((len(Scores) / 2))
Scores.insert(Index, 85)

print(Counter)
print(Scores)

"""
Output:
3
[56, 56, 78, 85, 88, 88, 92]
"""