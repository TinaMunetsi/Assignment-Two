# The Car class contains three attributes:
#
# 1. make
# 2. model
# 3. year
#
# The class also contains a method that returns a formatted
# description of the car.
#
# ElectricCar inherits from Car.
#
# ElectricCar introduces an additional battery_size attribute,
# which is initialized through its constructor.
#
# The description method is overridden so that the battery
# size is included in the description.
#
# ElectricCar also contains a method that provides additional
# information about the battery, including its size, charging
# time and range.


class Car:
    """
    Base class representing a general car.
    """

    def __init__(self, make, model, year):
        # Store the make of the car.
        self.make = make

        # Store the model of the car.
        self.model = model

        # Store the manufacturing year.
        self.year = year

    def description(self):
        """
        Return a formatted description of the car.
        """

        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):
    """
    Subclass representing an electric car.

    ElectricCar inherits the attributes and behaviour of Car
    and adds battery-related information.
    """

    def __init__(
        self,
        make,
        model,
        year,
        battery_size,
        charging_time=8,
        range_km=400
    ):
        # Call the constructor of the parent Car class.
        super().__init__(make, model, year)

        # Store the battery size.
        self.battery_size = battery_size

        # Store the estimated charging time.
        self.charging_time = charging_time

        # Store the estimated driving range.
        self.range_km = range_km

    def description(self):
        """
        Override the description method from the Car class.

        The returned description includes the battery size.
        """

        return (
            f"{self.year} {self.make} {self.model} "
            f"- Battery: {self.battery_size} kWh"
        )

    def battery_description(self):
        """
        Return a detailed description of the battery.
        """

        return (
            f"Battery size: {self.battery_size} kWh, "
            f"Charging time: {self.charging_time} hours, "
            f"Range: {self.range_km} km"
        )


# ------------------------------------------------------------
# Example usage of the Car class
# ------------------------------------------------------------

car = Car(
    "Toyota",
    "Corolla",
    2024
)

print("\nCar Description:")
print(car.description())


# ------------------------------------------------------------
# Example usage of the ElectricCar class
# ------------------------------------------------------------

electric_car = ElectricCar(
    "Tesla",
    "Model 3",
    2025,
    75,
    charging_time=6,
    range_km=500
)

print("\nElectric Car Description:")
print(electric_car.description())

print("\nBattery Description:")
print(electric_car.battery_description())