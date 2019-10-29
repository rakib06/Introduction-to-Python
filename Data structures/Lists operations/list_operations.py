animals = ['elephant', 'lion', 'tiger', "giraffe"]  # create new list
print(animals)

# add two items to the list
animals += ["monkey", 'dog']
print(animals)

# add one more item to the list using append() method
animals.append("dino")
print(animals)

# replace 'dino' with 'dinosaur'
animals[-1] = 'dinosaur'
print(animals)
