"""
Assignment 3: Division Program with Error Handling
This program asks for two numbers and divides them, with error handling and input validation.
"""

def get_valid_number(prompt):
    """
    Get a valid number from user input
    Returns the number if valid, None if invalid
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number!")
        return None

def main():
    print("Division Calculator")
    print("------------------")
    
    while True:
        # Get first number
        while True:
            num1 = get_valid_number("Enter first number: ")
            if num1 is not None:
                break
        
        # Get second number
        while True:
            num2 = get_valid_number("Enter second number: ")
            if num2 is not None:
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                break
        
        # Perform division
        try:
            result = num1 / num2
            print(f"\nResult: {num1} ÷ {num2} = {result}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Ask if user wants to continue
        while True:
            choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if choice in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'")
        
        if choice == 'no':
            print("\nThank you for using the Division Calculator!")
            break

if __name__ == "__main__":
    main() 