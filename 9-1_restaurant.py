class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"{self.restaurant_name} is a new restaurant opening on Main Street!")
        print(f"The restaurant specializes in {self.cuisine_type}-style food.")

    def open_restaurant(self):
        """Message indicates the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant("Shalaney O'Connor's", "Irish")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
