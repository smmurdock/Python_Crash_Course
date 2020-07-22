class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"{self.restaurant_name} is a new restaurant opening on Main Street!")
        print(f"The restaurant specializes in {self.cuisine_type}.")

    def open_restaurant(self):
        """Message indicates the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "raspberry",
                        "cream cheese", "blueberry", "snickers", "chocolate chip"]

    def display_flavors(self):
        """Display the flavors"""
        print("The available flavors are:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")


andys = IceCreamStand("Andy's", "Ice Cream")
andys.describe_restaurant()
andys.display_flavors()
