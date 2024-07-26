import numpy as np

def function1():
    # Function 1 code here
    result = np.sum(np.arange(2000))  # Different change to cause conflict
    print("Result of function1:", result)

def function2(x):
    # Function 2 code here
    result = np.prod(np.arange(1, x+1))
    print("Result of function2:", result)

def function3(x, y):
    # Function 3 code here
    s = function2(3)
    result = np.power(x, y) + np.sum(np.arange(s))
    print("Result of function3:", result)

def main():
    # Call the functions here
    function1()
    function2(5)
    function3(3, 7)

if __name__ == "__main__":
    main()
    def function4():
        # Function 4 code here
        result = np.mean(np.random.randint(1, 100, size=10))
        print("Result of function4:", result)
