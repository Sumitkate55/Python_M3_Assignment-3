# Task 1: Calculate Factorial Using a Function

def factorial(n):

    if n == 0:
        return 1
    else:
        # Use a loop to calculate the factorial
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")