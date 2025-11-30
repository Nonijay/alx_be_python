# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division, robustly handling ZeroDivisionError and ValueError 
    for non-numeric inputs.

    Parameters:
    - numerator (str): The numerator received as a string.
    - denominator (str): The denominator received as a string.

    Returns:
    - float or str: The result of the division or an error message.
    """
    try:
        # Attempt to convert arguments to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den
        return result

    except ZeroDivisionError:
        # Catch the specific error when the denominator is 0.0
        return "Error: Cannot divide by zero."

    except ValueError:
        # Catch the specific error when inputs cannot be converted to floats (non-numeric)
        return "Error: Please enter numeric values only."