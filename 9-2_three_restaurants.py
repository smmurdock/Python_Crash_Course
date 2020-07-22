class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"{self.restaurant_name} is a new restaurant opening on Atwood!")
        print(
            f"The restaurant specializes in {self.cuisine_type}-style food.\n")

    def open_restaurant(self):
        """Message indicates the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


ians_pizza = Restaurant("Ian's Pizza", "Italian")
tipsy_cow = Restaurant("Tipsy Cow", "American")
tex_tubbs = Restaurant("Tex Tubb's", "Mexican")

ians_pizza.describe_restaurant()
tipsy_cow.describe_restaurant()
tex_tubbs.describe_restaurant()
