# create new list
animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']
print(animals)

# replace 2 items -- 'lion' and 'tiger' with one item -- 'cat'
animals[1:3] = ['cat', 'rat', 'bat', 'Jerry']
print(animals)

# remove 2 items -- 'cat' and 'rat' from the list
animals[1:3] = []
print(animals)

copy_list = animals[-2:len(animals)]

# clear list
animals.clear()
print(animals)
print(copy_list)
