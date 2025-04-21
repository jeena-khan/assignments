#Q1. Write a program in python to create a list which is having 15 elements (5 integer, 5 float and 5 string values).

mylist = [1, 2, 3, 4, 5, 1.1, 1.2, 1.3, 1.4, 1.5, "operation", "completed", "successfully", "without", "errors"]

#Q2. Perform append operation on the list created above.

mylist.append("logged")
print(mylist)

#Q3. Create an empty list and add items using insert() operation.

empty_list = []
empty_list.insert(0,mylist[3]) ##### This will add the element at the 3rd index of mylist to the 0th index of empty_list #####
print(empty_list)

#Q4. Use for loop on list which you have created in question no.1.

for i in mylist:
  print(i)

#Q5. Write a program in python to create a list of 10 integer values and sort them in ascending and descending order?

sorting_list = [23, 42, 65, 11, 45, 67, 90, 64, 35, 72]
user = input("Type ascending or descending: ")
if user == "ascending":             ###### for ascending order #####
  sorting_list.sort(reverse = False)
  print(sorting_list)
else:                              ###### for descending order #####
  sorting_list.sort(reverse = True)
  print(sorting_list)

#Q6. Write a program in python to create a list of 10 random strings and sort them in ascending and descending order?

string_list = ["d", "h", "u", "r", "j", "s", "b", "p", "y", "k"]
user2 = input("Type ascending or descending: ")
if user2 == "ascending":             ###### for ascending order #####
  string_list.sort(reverse = False)
  print(string_list)
else:                              ###### for descending order #####
  string_list.sort(reverse = True)
  print(string_list)

#Q7. Create an empty list in python and add elements using insert function based on user choice (user will add position as well as element)?

user_list = []
user_position = int(input("At what index do you want to insert? "))
user_data = input("what do you want to insert in the list? ")
user_list.insert(user_position, user_data)
print(user_list)

#Q8. Write a program in python to find minimum and maximum element in a list?

value_list = list(input("enter integers: "))
user3 = input("maximum or minimum? ")
if user3 == "maximum":
  print(max(value_list))
else:                            
  print(min(value_list))

#Q9. Write a program in python to add list within list?

main_list = [1, 2, 3, 4]
nested_list = [5, 6, 7]
main_list.append(nested_list)
print(main_list)

#Q10. Write a program in python to create a list and perform Append() Insert() Remove() Pop() Copy(). 

last_list = list(input("make a list: "))
function = input("what function do you want to perfotm? (Enter Append, Insert, Remove, Pop or Copy) ")
if function == "append":
  append = input("add what? ")
  print(last_list.append(append))

elif function == "insert":
  insert_p = int(input("insert at index? "))
  insert_d = input("insert what? ")
  print(last_list.insert(insert_p, insert_d))

elif function == "remove":
  remove = input("remove what? ")
  print(last_list.remove(remove))

elif function == "pop":
  pop = int(input("pop index? "))
  print(last_list.pop(pop))

elif function == "copy":
  print(last_list.copy())
