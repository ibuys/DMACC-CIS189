"""
CIS189 Module 10 Encapsulation assignment script.
"""

class Employee:
    """
    Employee class.
    """
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


    def display(self):
        """
        Display employee information as:

            LAST_NAME, FIRST_NAME: <last name, first name here>
            PHONE_NUMBER: <phone number here>
            ADDRESS: <address here>
            START DATE: <start date here>
            SALARY: <salary here>
        """

        # Remove pass after you add your code.

        ##### YOUR CODE HERE #####
        pass


    




def main():

    person_list = [
        {"last_name": "VanRossum", "first_name": "Guido","address": "461 Ocean Blvd",
        "phone_number": "773-735-1849", "salary": 97500, "start_date": "1991-02-22"},

        {"last_name": "Haggard", "first_name": "Merle","address": "Bakersfield, CA",
        "phone_number": "484-765-2231", "salary": 72500, "start_date": "1967-11-08"},

        {"last_name": "Prine", "first_name": "John","address": "Paradise, KY",
        "phone_number": "743-435-8310", "salary": 88500, "start_date": "1995-07-31"},
        ]
    
    # Iterate over person_list, and create a new Employee instance and call the 
    # display method for each.

    ##### YOUR CODE HERE #####








if __name__ == "__main__":

    main()

