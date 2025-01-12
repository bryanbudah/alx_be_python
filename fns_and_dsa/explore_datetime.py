from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """
    Calculates and displays the date after adding a user-specified number of days to the current date.
    """
    try:
        # Prompt the user to enter the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"The date after {days_to_add} days will be: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

def main():
    """
    Main function to execute the datetime operations.
    """
    print("Exploring Python's datetime module")
    print("-" * 40)
    
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display a future date
    calculate_future_date()

if __name__ == "__main__":
    main()
else:
    print("curent date.")
