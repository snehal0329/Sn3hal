# Recursive method to calculate Fibonacci numbers
def recursive_fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case: sum of previous two Fibonacci numbers
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-recursive method to calculate Fibonacci numbers
def non_recursive_fibonacci(n):
    
    first = 0
    second = 1
    # Print the first n Fibonacci numbers
    print(first)
    print(second)
    for _ in range(n - 2):  # Loop starts from the third term
        third = first + second
        print(third)
        # Update values for the next iteration
        first = second
        second = third

# Main code
n = int(input("Enter the value of n: "))  # Change n to calculate more Fibonacci numbers if needed
if n<0:
        print("Enter positive value of n!")
else:
    print("Recursive Fibonacci:")
    for i in range(n):
        print(recursive_fibonacci(i))

    print("Non-Recursive Fibonacci:")
    non_recursive_fibonacci(n)
