from memorize import memorize
import sys

@memorize(10000)
def fibonacci(x: int):
    "0 1 1 2 3 5 8 .."
    if (x < 1):
        return 0
    if (x == 1):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)

@memorize()
def fib3(x: int):
    "0 0 1 1 2 4 7 .."
    if (x < 2):
        return 0
    if (x == 2):
        return 1
    return fib3(x - 1) + fib3(x - 2) + fib3(x - 3)

@memorize()
def factorial(x: int):
    if (x < 2):
        return 1
    return x * factorial(x - 1)

def unmemorized_fibonacci(x: int):
    "0 1 1 2 3 5 8 .."
    if (x < 1):
        return 0
    if (x == 1):
        return 1
    return unmemorized_fibonacci(x - 1) + unmemorized_fibonacci(x - 2)


@memorize()
def greeter(msg, name=None):
    if name is not None:
        print("greeter({}, name = {}): Hello, {}".format(msg, name, name))
    else:
        print("greeter({}, name = {}): No name provided".format(msg, name))
    return msg

@memorize(10)
def low_history_identity(x):
    print(f"low_history_identity({x})")
    return x

def main():
    print(f"sys.getrecursionlimit() = {sys.getrecursionlimit()}")
    n = min(int(input(f"INPUT n: int = ?, n < sys.getrecursionlimit() // 3 = {sys.getrecursionlimit() // 3}\n")), sys.getrecursionlimit() // 3)
    print("factorial({}) is {} digits long".format(n, len(str(factorial(n)))))
    print("fib3({})      is {} digits long".format(n, len(str(fib3(n)))))
    print("fibonacci({}) is {} digits long".format(n, len(str(fibonacci(n)))))
    print("factorial({}) is {} digits long".format(n, len(str(factorial(n)))))
    print("fib3({})      is {} digits long".format(n, len(str(fib3(n)))))
    print("fibonacci({}) is {} digits long".format(n, len(str(fibonacci(n)))))
    print("fibonacci(300) =", fibonacci(300))
    try:
        print("Press ctrl+C when you get bored waiting...")
        print("unmemorized_fibonacci(300) = ")
        print( unmemorized_fibonacci(300))
    except (RecursionError, KeyboardInterrupt):
        print('')


    print("UNCACHED GREETINGS BEGIN")
    greeter("Message 1") # greeted
    greeter("Message 2") # greeted 
    greeter("Message 3") # greeted 
    greeter("Message 4") # greeted 
    print("UNCACHED GREETINGS END\n")

    print("CACHED GREETINGS BEGIN")
    greeter("Message 1") # not greeted, memorized
    greeter("Message 2") # not greeted, memorized
    greeter("Message 3") # not greeted, memorized
    greeter("Message 4") # not greeted, memorized
    print("CACHED GREETINGS END\n")

    print("UNCACHED KVARGS GREETINGS BEGIN")
    greeter("Message 1", "Andrew") # greeted
    greeter("Message 2", "Andrew") # greeted 
    greeter("Message 3", "Andrew") # greeted 
    greeter("Message 4", "Andrew") # greeted 
    print("UNCACHED KVARGS GREETINGS END\n")

    print("CACHED KVARGS GREETINGS BEGIN")
    greeter("Message 1", "Andrew") # not greeted, memorized 
    greeter("Message 2", "Andrew") # not greeted, memorized  
    greeter("Message 3", "Andrew") # not greeted, memorized  
    greeter("Message 4", "Andrew") # not greeted, memorized  
    print("CACHED KVARGS GREETINGS END\n")

    for i in range(5, 15):
        print("i =", i)
        for j in range(i):
            low_history_identity(j)
    

if __name__ == "__main__":
    main()
