# File Name : driver.py
# Student Name: Cole Crooks
# email: crookscl@mail.uc.edu  
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS 4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Each team member contributes at least one class (except the member who writes the main.py file). Classes must include __init__, __str__, and __repr__ methods, 
# at least one property with getters and setters, and one functional method.

# Brief Description of what this module does. The main method serves as the entry point for the program. It creates objects from the defined classes, 
# demonstrates their functionalities by calling both special (dunder) and regular methods, 
# and prints relevant information to showcase all required class features in a clear and organized way.
# Citations: https://chatgpt.com/

class Driver:
    def __init__(self, name: str, license_valid: bool):
        """Initialize the Driver object with name and license validity."""
        self.name = name
        self._license_valid = license_valid  # Using _license_valid to enable property getter/setter

    def __str__(self):
        """Return a human-readable string representation of the Driver."""
        return f"{self.name} (License: {'Valid' if self.license_valid else 'Invalid'})"

    def __repr__(self):
        """Return a detailed string representation useful for debugging."""
        return f"Driver(name='{self.name}', license_valid={self.license_valid})"

    @property
    def license_valid(self):
        """Getter for the driver's license status."""
        return self._license_valid

    @license_valid.setter
    def license_valid(self, status: bool):
        """Setter for the driver's license status."""
        if isinstance(status, bool):
            self._license_valid = status
        else:
            raise ValueError("License validity must be a boolean value.")

    def drive_car(self, car):
        """Drive the car if the driver's license is valid."""
        if self.license_valid:
            print(f"{self.name} is driving the {car.make} {car.model}.")
            car.start_engine()  # Make sure the car's engine is started before driving
        else:
            print(f"{self.name} cannot drive. License is invalid.")
