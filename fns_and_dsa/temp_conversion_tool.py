# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    """Main function to interact with the user and perform conversions."""
    try:
        # Prompt user for input
        temperature_input = input("Enter the temperature (e.g., 100 C or 212 F): ").strip()
        
        # Check if the input ends with 'C' for Celsius or 'F' for Fahrenheit
        if temperature_input[-1].upper() == 'C':
            celsius = float(temperature_input[:-1].strip())  # Extract numeric value and convert to float
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        
        elif temperature_input[-1].upper() == 'F':
            fahrenheit = float(temperature_input[:-1].strip())  # Extract numeric value and convert to float
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        
        else:
            raise ValueError("Invalid temperature format. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
