# --- Global Conversion Factors ---
# Define the constants at the top level, making them globally accessible.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Factor for (F - 32) * (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Factor for (C * 9/5) + 32

# --- Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: (F - 32) * (5/9)
    """
    # The function automatically reads the global variable's value
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: (C * 9/5) + 32
    """
    # The function automatically reads the global variable's value
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# --- Main Logic and User Interaction ---

def main():
    print("Welcome to the Temperature Conversion Tool!")
    
    # Get and validate the temperature input
    while True:
        temp_input = input("Enter the temperature value: ")
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error message for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Get and validate the unit input
    unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

    print("-" * 30)

    # Call the appropriate conversion function
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
        
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
        
    else:
        print("Invalid unit specified. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")