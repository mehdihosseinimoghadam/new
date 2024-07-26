import numpy as np
def function1():
    # Function 1 code here
    result = 2 + 3
    print("Result of function1:", result)

def function2(x):
    # Function 2 code here
    result = 5 - 2 + x
    print("Result of function2:", result)

def function3(x, y):
    # Function 3 code here
    s = function2(3)
    result = 3+x * y^7 + s
    print("Result of function3:", result)

def main():
    # Call the functions here
    function1()
    function2()
    function3(3,7, 6)

if __name__ == "__main__":
    main()