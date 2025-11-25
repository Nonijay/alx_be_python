from datetime import datetime

def display_current_datetime():
    current_date = datetime.now()
    #format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%D %H:%M:%S")
    print("\nPart 1: current Date and Time")

    print(f"The current date and time is {formatted_date}")

def calculate_future_date ():
    #prompt the user to enter a number of days as an integer

    try:
        days_input = input("Enter a number of days to add: ")
        num_days = int(days_input)
    except ValueError:
        print("Invalid input. Please enter a whole number. ")
        return #Exit the function if input is invalid
    
    # Get the current date (time component is optional for calculation)
    current_day = datetime.today()
    
    # Create a timedelta object representing the specified number of days
    time_delta = datetime.timedelta(days=num_days)

    # Calculate what the date will be after adding the specified number of days
    # Saves the future date inside a future_date variable
    future_date = current_day + time_delta

    # Print the future date in a format like “YYYY-MM-DD”
    formatted_future_date = future_date.strftime("%Y-%m-%D")
    print(f"Date after adding {num_days} days: {formatted_future_date}")

# --- Main Execution Block ---

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
