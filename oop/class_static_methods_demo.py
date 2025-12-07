class Calculator:
    """
    A class demonstrating the use and difference between static methods 
    and class methods in Python.
    """
    
    # Class Attribute: Accessible by class methods (via 'cls')
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Performs a calculation without access to the class 
        or the instance. It's just a function logically grouped within the class.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Receives the class itself (cls) as the first argument, 
        allowing it to access and modify class attributes.
        """
        # Accessing the class attribute 'calculation_type' via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b