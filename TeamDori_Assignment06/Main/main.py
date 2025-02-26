




"""
from car import Car
from driver import Driver

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
"""