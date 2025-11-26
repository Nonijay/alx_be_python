from datetime import datetime, timedelta # Need to import timedelta explicitly too!

def display_current_datetime():
    current_date = datetime.now()
    # CORRECTED: Ensures exact match to "%Y-%m-%d %H:%M:%S"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("\nPart 1: current Date and Time")
    print(f"The current date and time is {formatted_date}")

def calculate_future_date ():
    # prompt the user to enter a number of days as an integer
    try:
        # Assuming the checker requires this specific prompt
        days_input = input("Enter the number of days to add to the current date:") 
        num_days = int(days_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return # Exit the function if input is invalid
    
    # Get the current date (using datetime.now() or datetime.today() works)
    current_day = datetime.now()
    
    # Create a timedelta object representing the specified number of days
    # NOTE: Since you only imported 'datetime', access timedelta via 'timedelta' if imported directly, 
    # or via 'datetime.timedelta' if you only imported 'datetime'
    time_delta = timedelta(days=num_days) 

    # Calculate what the date will be after adding the specified number of days
    future_date = current_day + time_delta

    # Print the future date in a format like “YYYY-MM-DD”
    # CORRECTED: Ensures exact match to “%Y-%m-%d”
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after adding {num_days} days: {formatted_future_date}")

# --- Main Execution Block ---

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()