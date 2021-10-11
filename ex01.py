def plus_five(x):
    """
    this function takes a number (x) and returns its value plus 5
    """

    #return x + 5
    #x = x + 5
    x += 5
    return x

def add_ten(x):
    """
    updates a list of numbers to be +10
    x - the list of numbers
    """

    # for i,v in enumerate(x):
    #     x[i] = v + 10

    # for v in x: # <-- won't work
    #     v += 10

    for i in range(len(x)):
        # x[i] = x[i] + 10
        x[i] += 10


some_number = 10
print("some number before:", some_number)
print("plus five result:", plus_five(some_number)) # will print 15
print("some number after:", some_number)

some_number = plus_five(some_number)
print('after operation: "some_number = plus_five(some_number)"')
print("some number =", some_number)

print()

num_list = [1, 2, 3, 4, 5]
print("num list before:", num_list)
add_ten(num_list)
print("num list after :", num_list)