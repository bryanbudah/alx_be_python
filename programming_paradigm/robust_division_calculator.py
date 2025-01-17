# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with error handling for:
    - Division by zero
    - Non-numeric inputs
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = num / den
        return f"The result of the division is {result:.2f}"
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
