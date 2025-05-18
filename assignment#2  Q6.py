#Q6. Write a program in python to create a dictionary of 10 elements and delete item using popitems() function ?
mydictionary = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
    "f": 60,
    "g": 70,
    "h": 80,
    "i": 90,
    "j": 100
}

print("Original Dictionary:")
print(mydictionary)

removed_item = mydictionary.popitem()

print("\nDictionary after using popitem():")
print(mydictionary)

print("\nRemoved item:")
print(removed_item)
