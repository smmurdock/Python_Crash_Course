class User:
    """Create a simple user profile"""

    def __init__(self, first_name, last_name, username, age, location):
        """Define first name, last name, username, age, and location attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        # assigned as a default value rather than as a parameter
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


jackson_pollack = User("Jackson", "Pollack", "jpollack", 35, "Seattle, WA")
jackson_pollack.increment_login_attempts()
jackson_pollack.increment_login_attempts()
print(jackson_pollack.login_attempts)
jackson_pollack.reset_login_attempts()
print(jackson_pollack.login_attempts)
