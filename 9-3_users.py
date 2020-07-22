class User:
    """Create a simple user profile"""

    def __init__(self, first_name, last_name, username, age, location):
        """Define first name, last name, username, age, and location attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location

    def describe_user(self):
        """Use the attributes to describe the user"""
        print(
            f"User: {self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        """Greet the user using the given name"""
        print(f"Hello, {self.first_name}! Welcome back!\n")


shanay_murdock = User("Shanay", "Murdock", "smurdock", 31, "Columbia, MO")
sam_tarly = User("Sam", "Tarley", "samtarley", 28, "Chicago, IL")
todd_jones = User("Todd", "Jones", "tmjones", 47, "Portland, OR")

shanay_murdock.describe_user()
shanay_murdock.greet_user()

sam_tarly.describe_user()
sam_tarly.greet_user()

todd_jones.describe_user()
todd_jones.greet_user()
