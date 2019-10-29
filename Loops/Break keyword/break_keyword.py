count = 0

# this condition cannot possibly be false
while True:
    print(count)
    count += 1
    if count >= 5:
        break
        # exit loop if count >= 5


zoo = ["lion", 'tiger', 'elephant']
# this condition cannot possibly be false
while True:
    # extract one element from the list end
    animal = zoo.pop()
    print(animal)
    # if exit loop if animal is 'elephant':
    if animal == 'lion':
        break
        # exit loop
