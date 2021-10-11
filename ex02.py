#usually you dpn't include operation code before
#functions definitions. we add this here so
#that we can break the debugger before the
#creation of the functions.
print("program start. creating functions.")

def f1():
    print("function one START")
    print("function one END")

def f2():
    print("function two START")
    print("calling f1...")
    f1()
    print("function two END")

def f3():
    print("function three START")
    print("calling f2...")
    f2()
    print("function three END")


print("functions created. starting main code.")
print("calling f3 from main code...")
f3()
print("calling f2 from main code...")
f2()
print("program end")
