class User:
    """Create a simple user profile"""

    def __init__(self, first_name, last_name, username, age, location):
        """Define first name, last name, username, age, and location attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Use the attributes to describe the user"""
        print(
            f"User: {self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        """Greet the user using the given name"""
        print(f"Hello, {self.first_name}! Welcome back!\n")

    def increment_login_attempts(self):
        """Increment the login attempts by 1 each time a user attempts to log in"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0"""
        self.login_attempts = 0


class Admin(User):
    """An administrator is a special kind of User"""

    def __init__(self, first_name, last_name, username, age, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = ["can add post",
                           "can delete post", "can ban user", "can pin post"]

    def show_privileges(self):
        """Display the list of privileges"""
        print(f"{self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"--{privilege}")


josh_k = Admin("Josh", "Kirkland", "jkirkland", 28, "Richmond, VA")
josh_k.show_privileges()
