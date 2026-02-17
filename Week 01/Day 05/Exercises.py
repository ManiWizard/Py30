# ███▓▒░  Day 5: Py30 Exercises  ░▒▓███

"""
TODO — Day 5 Exercises Overview

[x] Exercise A : Declare an empty list

[x] Exercise B : Create a list with more than 5 items
[x] Exercise B : Find the length of your list
[x] Exercise B : Get the first, middle, and last item of the list

[x] Exercise C : Declare mixed_data_types with name, age, height, marital status, address

[x] Exercise D : Declare it_companies with initial values
[x] Exercise D : Print the it_companies list
[x] Exercise D : Print the number of companies
[x] Exercise D : Print the first, middle, and last company
[x] Exercise D : Modify one company
[x] Exercise D : Add an IT company
[x] Exercise D : Insert an IT company in the middle
[x] Exercise D : Change one company name to uppercase (excluding IBM)
[x] Exercise D : Join it_companies with '#;  '
[x] Exercise D : Check if a company exists in the it_companies list.
[x] Exercise D : Sort the list using sort()
[x] Exercise D : Reverse the list in descending order using reverse()
[x] Exercise D : Slice out the first 3 companies
[x] Exercise D : Slice out the last 3 companies
[x] Exercise D : Slice out the middle company or companies
[x] Exercise D : Remove the first IT company
[x] Exercise D : Remove the middle IT company or companies
[x] Exercise D : Remove the last IT company
[x] Exercise D : Remove all IT companies
[x] Exercise D : Destroy the IT companies list

[x] Exercise E : Join front_end and back_end lists
[x] Exercise E : Copy joined list into full_stack and insert Python and SQL after Redux
"""

# # Exercise A
#   - 1. Declare an empty list
# This creates a list with no elements inside it.
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Empty_List = []  # Empty list literal

print(Empty_List)  # Output should be: []


# # Exercise B
#   - 2. Declare a list with more than 5 items
#   - 3. Find the length of your list
#   - 4. Get the first item, the middle item and the last item of the list
# This section demonstrates indexing and length calculation.
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Random_List = ["This", "is", "a", "Random", "list", "of", "items"]  # 7 elements
Random_List_Len = len(Random_List)  # Total number of elements

Random_List_First = Random_List[0]  # First element (index 0)
Random_List_Middle = Random_List[Random_List_Len // 2]  # Middle element using integer division
Random_List_Last = Random_List[-1]  # Last element using negative indexing

print(Random_List)
print(Random_List_Len)
print(Random_List_First)
print(Random_List_Middle)
print(Random_List_Last)


# # Exercise C
#   - 5. Declare a list called mixed_data_types
# This list contains multiple data types (string, int, float).
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Mixed_Data_Types = ["Mani", 23, 1.75, "Golestan, Iran"]  # Mixed types in one list


# # Exercise D
#   - 6-25. Working with it_companies list
# This section demonstrates mutation, slicing, sorting, joining, and deletion.
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(Companies)  # Print full list

print(len(Companies)+1)  # Print length (+1 as written in original code)

# Accessing first, middle, and last items
print(Companies[0])
print(Companies[len(Companies) // 2])
print(Companies[-1])

# Modify first company
Companies[0] = "Meta"
print(Companies)

# Add a company to the end
Companies.append("Cloudflare")
print(Companies)

# Insert company in the middle using index lookup
Companies.insert(Companies.index(Companies[len(Companies) // 2]), "Proton")
print(Companies)

# Convert first company name to uppercase
Companies[0] = Companies[0].upper()
print(Companies)

# Join list elements into a single string with custom separator
Companies_Joined = '#;  '.join(Companies)
print(Companies_Joined)

# Check membership (boolean result)
print("META" in Companies)

# Sort alphabetically (in-place)
Companies.sort()
print(Companies)

# Reverse order (in-place)
Companies.reverse()
print(Companies)

# Slice operations
print(Companies[0:3])  # First 3 companies
print(Companies[-3:])  # Last 3 companies
print(Companies[len(Companies) // 2-1:len(Companies) // 2+2])  # Middle slice

# Remove first company (by value)
Companies.remove(Companies[0])
print(Companies)

# Remove middle slice using del
del Companies[len(Companies) // 2 -1:len(Companies) // 2 +2]
print(Companies)

# Remove last company (by value reference)
Companies.remove(Companies[-1])
print(Companies)

# Clear all elements
Companies.clear()
print(Companies)

# Destroy the variable entirely
del Companies


# # Exercise E
#   - 26. Join front_end and back_end lists
#   - 27. Copy joined list into full_stack and insert Python and SQL after Redux
# This section demonstrates list concatenation and insertion by index.
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
Back_end = ['Node','Express', 'MongoDB']

Fullstack = Front_end + Back_end  # Concatenate two lists
print(Fullstack)

Redux_Index = Fullstack.index("Redux")  # Find index of 'Redux'
print(Redux_Index)

# Insert new technologies after Redux
Fullstack.insert(Redux_Index+1, "Python")
Fullstack.insert(Redux_Index+2, "SQL")
print(Fullstack)
