def f1():
    print("function one START")
    x = 100
    print("f1:x:", x)
    print("function one END")


def f3():
    print("function three START")
    x = y
    print("f3:x:", x)
    f2()
    print("f3:x:", x)
    print("function three END")


def f2():
    print("function two START")
    x = 33
    print("f2:x:", x)
    f1()
    print("f2:x:", x)
    print("function two END")


print("starting main code.")
y = 10
print("calling f3 from main code...")
f3()
print("calling f2 from main code...")
f2()
print("program end")
