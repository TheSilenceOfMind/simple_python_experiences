class Employee():
    """This class describes Employee and it's salary"""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add=5000):
        """give_raise increases salary of the employee"""
        self.salary += add