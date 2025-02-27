# File Name : main.py
# Student Name: Ryan Jacob
# email:  Jacobry@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:  2/20/2025
# Course #/Section:  IS4010-002
# Semester/Year:  Spring 2025
# Brief Description of the assignment:  his assignment involves collaborating with peers to create a Python-based project that models a real-world concept. 
# Each team member contributes at least one class (except the member who writes the main.py file). Classes must include __init__, __str__, and __repr__ methods, 
# at least one property with getters and setters, and one functional method.

# The main method serves as the entry point for the program. It creates objects from the defined classes, 
# demonstrates their functionalities by calling both special (dunder) and regular methods, 
# and prints relevant information to showcase all required class features in a clear and organized way.
# Citations: https://chatgpt.com/





from car.geierml_car import *
from driver.crookscl_driver import *


def main():
    # 1. Instantiate at least one object of each type
    my_car = Car(make="Toyota", model="Camry", color="Blue")
  
    my_driver = Driver(name="Alice", license_valid=True)

    # 2. Demonstrate __str__ and __repr__ usage
    print("STRING REPRESENTATIONS:")
    print(str(my_car))      # calls Car.__str__()
    print(str(my_driver))   # calls Driver.__str__()
    print("\nREPR REPRESENTATIONS:")
    print(repr(my_car))     # calls Car.__repr__()
    print(repr(my_driver))  # calls Driver.__repr__()

    # 3. Demonstrate custom methods
    print("\nDEMONSTRATING METHODS:")
    my_car.start_engine()   # engine is off by default, so start it
    my_car.start_engine()   # try to start again to show it won't duplicate

    my_car.repaint("Red")   # show color change method

    # 4. Use the Driver to drive the Car
    my_driver.drive_car(my_car)
 
    # 5. Show property getters and setters in action
    print("\nCHECKING/SETTING PROPERTIES:")
    print(f"Current car color: {my_car.color}")
    my_car.color = "Black"
    print(f"New car color: {my_car.color}")
  
    print(f"Driver license status: {my_driver.license_valid}")
    my_driver.license_valid = False
    print(f"Driver license status after change: {my_driver.license_valid}")

    # Try driving again with invalid license
    my_driver.drive_car(my_car)
    

if __name__ == "__main__":
    main()
