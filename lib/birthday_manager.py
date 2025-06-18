
from datetime import datetime 
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

    def _dob_string_converter(self, dob):
        dob_dt = datetime.strptime(dob, "%Y-%m-%d")
        return dob_dt

    def _dob_dt_converter(self, dob_dt):
        dob_str = dob_dt.strftime("%Y-%m-%d")
        return dob_str
    
    def upcoming_birthdays(self):

        today_dt = datetime.today()
        this_month = today_dt.month
        next_month = this_month + 1
        
        birthday_dict_list = [
                            {
                                friend: self._dob_string_converter(birthday)
                            } 
                                for friend, birthday in self.manager.items()
                            ]

        upcoming_list = []
        for item in birthday_dict_list:                 # list of dictionaries
            month = list((item.values()))[0].month      # unpacked view object 
            day = list((item.values()))[0].day          # unpacked view object 
            if month == this_month and day > today_dt.day or month == next_month:
                name_key = list(item.keys())[0]         # unpacked view object 
                birthday_str = self._dob_dt_converter(list((item.values()))[0]) # unpacked view object passed to dt_converter
                upcoming_list.append({name_key: birthday_str})
                
        return  upcoming_list 



        

    def upcoming_age_calculator(self):
         # Parameters:
        #    None
        # Returns:
        #   A list of friends + upcoming ages
        # Side-effects:
        #   None
        
        pass # No code here yet