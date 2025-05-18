#Q5. Write a program in python to create a dictionary of 10 elements and print values using values () functions?
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

print("The values in the dictionary are:")
for value in mydictionary.values():
    print(value)