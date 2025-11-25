# --- Global Conversion Factors ---
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# --- Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# --- Main Logic and User Interaction ---

def main():
    print("Welcome to the Temperature Conversion Tool!")
    
    # Input Validation and Prompt 1 (Strict Match Required)
    while True:
        temp_input = input("Enter the temperature to convert:").strip()
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error message for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Input Prompt 2 (Strict Match Required)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

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