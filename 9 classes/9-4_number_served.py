class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # assigned as a default value rather than as a parameter
        self.number_served = 0

    def describe_restaurant(self):
        """Description of the restaurant"""
        print(f"{self.restaurant_name} is a new restaurant opening on Main Street!")
        print(f"The restaurant specializes in {self.cuisine_type}-style food.")

    def open_restaurant(self):
        """Message indicates the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

    def view_number_served(self):
        """Print out the number of total clients served"""
        print(f"This restaurant has served {self.number_served} guests.")

    def set_number_served(self, served):
        """Set the number of customers served"""
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You can't lower the number of guests served.")

    def increment_number_served(self, guests):
        """Add the given number of guests to the number of guests served"""
        if guests > 0:
            self.number_served += guests
        else:
            print("You can't lower the number of guests served.")


restaurant = Restaurant("Tex Tubb's", "Mexican")
restaurant.view_number_served()

restaurant.set_number_served(10)
restaurant.view_number_served()

restaurant.increment_number_served(6)
restaurant.view_number_served()
