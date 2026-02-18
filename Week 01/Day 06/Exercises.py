# ███▓▒░  Day 6: Py30 Exercises  ░▒▓███

"""
TODO — Day 6 Exercises Overview
"""

# # Exercise A
#   - Exercises: Level 1
#       01. Create an empty tuple
#       02.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#       03.Join brothers and sisters tuples and assign it to siblings
#       04.How many siblings do you have?
#       05.Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Empty_Tuple = tuple()

Parents  = ("Mohammad", "Malihe",)
Brothers = tuple()
Sisters  = ("Farima",)

Siblings = Brothers + Sisters
Family_Members =  Parents + Siblings

Counter = len(Family_Members)

print(f"How many people are in your Family? {Counter}")
print(f"Family: {", ".join(Family_Members)}")

print()

# # Exercise A

# Exercises: Level 2
#   - 01.Unpack siblings and parents from family_members
#   - 02.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
#   - 03.Change the about food_stuff_tp tuple to a food_stuff_lt list
#   - 04.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
#   - 05.Slice out the first three items and the last three items from food_stuff_lt list
#   - 06.Delete the food_stuff_tp tuple completely
#   - 07.Check if an item exists in tuple:
#       - Check if 'Estonia' is a nordic country
#       - Check if 'Iceland' is a nordic country
#           nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("◆━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◆")

Father, Mother, Sister = Family_Members

print(Father)
print(Mother)
print(Sister)

Fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry")
Vegetables = ("Asparagus", "Broccoli", "Carrot", "Kale", "Spinach")
Animal_products = ("Egg", "Honey", "Milk", "Beef", "Salmon")

food_stuff_tp = Fruits + Vegetables + Animal_products

print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt[len(food_stuff_lt) // 2])
# or
print(food_stuff_lt[len(food_stuff_lt) // 2 - 1: len(food_stuff_lt) // 2 + 2])

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp


Nord = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in Nord)
print("Iceland" in Nord)