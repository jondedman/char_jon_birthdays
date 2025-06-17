
class BirthdayManager:
    # User-facing properties:
    #   name: string
    #   birthday: string (YYYY-MM-DD)

    def __init__(self):
        self.manager = {}

    def __dob_format_checker(self, date_of_birth):
        if len(date_of_birth) == 10 and date_of_birth[4] == '-':
            year = date_of_birth[0:4]
            month = date_of_birth[5:7]
            day = date_of_birth[8:10]
            return year.isnumeric() and month.isnumeric() and day.isnumeric()

        return False

    def add(self, name, dob):
        if name == "":
            raise Exception("Name cannot be empty string!")
        if self.__dob_format_checker(dob) == False:
            raise Exception("Warning! DOB format incorrect!")

        self.manager[name] = dob


    def update_birthday(self, name, new_date):
         # Parameters:
        #   name: string representing a friend's name
        #   new_date:  string representing a friend's updated dob (YYY-MM-DD)
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend's birthday with the new birthday date to the self object
        #   Throws exception if name doesn't exist in Birthday Manager

        pass # No code here yet

    def update_name(self, name, new_name):
         # Parameters:
        #   name: string representing a friend's name
        #   new_name: string representing a friend's updated name
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend's name with the new name to the self object
        #   Throws exception if name doesn't exist in Birthday Manager
        #   Throws exception if new_name is an empty string

        pass # No code here yet

    def upcoming_birthdays(self):
         # Parameters:
        #    None
        # Returns:
        #   List of friends + birthdays for the birthdays coming up in the next 30 days
        # Side-effects
        #   None

        pass # No code here yet

    def upcoming_age_calculator(self):
         # Parameters:
        #    None
        # Returns:
        #   A list of friends + upcoming ages
        # Side-effects:
        #   None
        
        pass # No code here yet