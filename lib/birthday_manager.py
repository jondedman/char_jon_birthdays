
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
        if self.manager.get(name) == None:
            raise Exception("No friend with that name")
        if self.__dob_format_checker(new_date) == False:
            raise Exception("Warning! new_date format incorrect!")        
        self.manager[name] = new_date

    def update_name(self, name, new_name):
        if new_name == "":
            raise Exception("new_name cannot be empty string!")
        if self.manager.get(name) == None:
            raise Exception("No friend with that name")
        self.manager[new_name] = self.manager[name]
        del self.manager[name]


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