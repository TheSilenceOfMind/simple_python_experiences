import unittest as ut
from class_testing_11_3.employee import Employee


class TestEmployee(ut.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create an employee
        """
        self.salary = 100
        self.employee = Employee('Irina', 'Korolik', self.salary)

    def test_give_default_raise(self):
        """
        Test that salary is raised up by default value
        """
        self.salary += 5000
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary)

    def test_give_custom_raise(self):
        """
        test that salary is raised up by custom value
        """
        self.salary += 1300
        self.employee.give_raise(1300)
        self.assertEqual(self.employee.salary, self.salary)

        self.salary -= 500
        self.employee.give_raise(-500)
        self.assertEqual(self.employee.salary, self.salary)

        self.salary += 0
        self.employee.give_raise(0)
        self.assertEqual(self.employee.salary, self.salary)
