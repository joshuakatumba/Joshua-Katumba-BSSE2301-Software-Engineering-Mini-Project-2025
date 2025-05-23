"""
Assignment 2: Factorial Calculator
This program calculates the factorial of the number 5.
"""

def calculate_factorial(n):
    """
    Calculate the factorial of a number using recursion
    """
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

def main():
    number = 5
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")
    
    # Print the calculation steps
    print("\nCalculation steps:")
    steps = []
    for i in range(number, 0, -1):
        steps.append(str(i))
    print(" × ".join(steps), "=", result)

if __name__ == "__main__":
    main() 