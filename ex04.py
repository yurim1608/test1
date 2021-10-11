def f1():
    y = x
#     y += 5
#     x = y


def f2():
    x = 13  # hiding the global x by creating a local x
    y = x


def f3():
   global x
   x = 20


print("MAIN CODE:")
x = 10
david = "Hello"
# f1()
print("before:", x)
f2()
print("after:", x)

