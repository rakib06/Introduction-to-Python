# create new dictionary.
#  "John", "Jane" and "Jerard" are keys and numbers are values
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}

print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book
del phone_book['John']

# print(Jane's phone)
print(phone_book['Jane'])