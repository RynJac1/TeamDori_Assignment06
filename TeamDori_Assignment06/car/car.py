
# car.py
# Madison Geier
# geierml@mail.uc.edu
#  Assignment 06
# 2/25/25
#  IS4010-002
#  Spring 2025
#  collaborating with peers to create a Python-based project that models a real-world concept. 
# Each team member contributes at least one class (except the member who writes the main.py file). Classes must include __init__, __str__, and __repr__ methods, 
# at least one property with getters and setters, and one functional method.

# The main method serves as the entry point for the program. It creates objects from the defined classes, 
# demonstrates their functionalities by calling both special (dunder) and regular methods, 
# and prints relevant information to showcase all required class features in a clear and organized way.
# Citations: https://chatgpt.com/

class Car:
    def __init__(self, make: str, model: str, color: str):
        """Initialize a Car object with make, model, and color."""
        self.make = make
        self.model = model
        self._color = color  # Using _color to enable property setter/getter
        self.engine_on = False  # Engine state defaults to off

    def __str__(self):
        """Return a human-readable string representation of the Car."""
        return f"{self.color} {self.make} {self.model} (Engine {'On' if self.engine_on else 'Off'})"

    def __repr__(self):
        """Return a detailed string representation useful for debugging."""
        return f"Car(make='{self.make}', model='{self.model}', color='{self.color}', engine_on={self.engine_on})"

    @property
    def color(self):
        """Getter for car color."""
        return self._color

    @color.setter
    def color(self, new_color):
        """Setter for car color."""
        if isinstance(new_color, str) and new_color:
            self._color = new_color
        else:
            raise ValueError("Color must be a non-empty string.")

    def start_engine(self):
        """Start the car's engine if it is not already running."""
        if not self.engine_on:
            self.engine_on = True
            print(f"The {self.color} {self.make} {self.model} engine has started.")
        else:
            print(f"The {self.color} {self.make} {self.model} engine is already on.")

    def repaint(self, new_color: str):
        """Change the car's color."""
        try:
            self.color = new_color  # Uses the setter
            print(f"The car has been repainted {self.color}.")
        except ValueError as e:
            print(f"Failed to repaint: {e}")
