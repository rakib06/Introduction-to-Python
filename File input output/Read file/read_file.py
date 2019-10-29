# here we open file "input.txt". Second argument used to identify that we want to read file
# Note: if you want to write to the file use "w" as second argument

f = open("input.txt", "r")

for line in f.readlines():   # read lines
    # print each line
    print(line)

# It's important to close the file to free up any system resources.
f.close()

f1 = open("input1.txt", "r")

# print only first line of f1
lines = []
for line in f1.readlines():
    lines.append(line)
print(lines[0])

# do not forget to close file
f1.close()
f1.close()