def multiply_by(a, b=2):
    return a * b


print(multiply_by(3, 47))
# call function using default value for b parameter
print(multiply_by(3))


# def hello(add parameters for function, set default value for name):
def hello(subject, name='Rakib'):
    print("Hello %s! My name is %s" % (subject, name))


# call 'hello' function with "PyCharm as a subject parameter and "Jane" as a name
hello("PyCharm", "Jane")
# call 'hello' function with "PyCharm as a subject parameter and default value for the name
hello("PyCharm")
