#Q7. Write a program in python to create a dictionary and add list as values?
# Creating a dictionary with lists as values
mydictionary = {
    "fruits": ["apple", "banana", "mango"],
    "vegetables": ["carrot", "broccoli", "spinach"],
    "drinks": ["water", "juice", "soda"]
}

print("Dictionary with lists as values:")
for key, value in mydictionary.items():
    print(f"{key}: {value}")
