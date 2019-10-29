hello_world = "Hello, World!"

for ch in hello_world:    # print each character from hello_world
    print(ch)

# initialize length variable
length = 0

# count how many characters are in the hello_world using loop
for ch in hello_world:
    length += 1     # add 1 to the length on each iteration

print(len(hello_world) == length)
