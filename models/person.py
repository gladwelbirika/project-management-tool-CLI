class Person:
    """
    Base class for all users in the system.
    """

    def __init__(self, name, email):
        self.name = name
        self._email = email

    @property
    def email(self):
        """
        Returns the user's email.
        """
        return self._email

    @email.setter
    def email(self, new_email):
        """
        Updates the user's email.
        """
        self._email = new_email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"