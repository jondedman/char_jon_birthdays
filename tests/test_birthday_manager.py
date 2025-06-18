from lib.birthday_manager import BirthdayManager
import pytest
from datetime import datetime

def test_Birthday_Manager_instance_has_empty_dictionary():
    birthdays = BirthdayManager()
    assert birthdays.manager == {}

"""
Given a name and a DOB
adds friend and birthday pair to manager dictionary
"""
def test_add_inserts_new_friend_and_birthday_into_manager():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    assert birthdays.manager == {"Char": "1993-11-17"}
    birthdays.add("Jon", "1976-09-11")
    assert birthdays.manager == {"Char": "1993-11-17", "Jon": "1976-09-11"}

"""
Given an empty string and a DOB
raises an exception => "Name cannot be empty string!"
"""
def test_add_empty_string_raises_an_exception():
    birthdays = BirthdayManager()
    with pytest.raises(Exception) as error:
        birthdays.add("", "1993-11-17")
    error_message = str(error.value)
    assert error_message == "Name cannot be empty string!"

"""
Given a name and an incorrectly-formatted DOB
raises an exception => "Warning! DOB format incorrect!"
"""
def test_add_incorrectly_formatted_string_raises_an_exception():
    birthdays = BirthdayManager()
    with pytest.raises(Exception) as error:
        birthdays.add("Jon", "19760911")
    error_message = str(error.value)
    assert error_message == "Warning! DOB format incorrect!"



"""
Given a name and new date of birth.
It updates corresponding entry in birthday manager
"""

def test_update_birthday_updates_key_value_pair():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    birthdays.update_birthday("Char", "2000-03-09")
    assert birthdays.manager["Char"] == "2000-03-09"


"""
Given a name not in birthday manager
It raises Exception => "No friend with that name"
"""

def test_update_birthday_raises_error_when_name_not_found():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    with pytest.raises(Exception) as error:
        birthdays.update_birthday("Jon", "2000-03-09")
    error_message = str(error.value)
    assert error_message == "No friend with that name"

"""
Given a new_date with the incorrect format
It raises Exception => "Warning! new_date format incorrect!"
"""

def test_update_birthday_raises_error_when_new_date_is_incorrect_formatt():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    with pytest.raises(Exception) as error:
        birthdays.update_birthday("Char", "20000309")
    error_message = str(error.value)
    assert error_message == "Warning! new_date format incorrect!"

"""
Given a new name for an entry
It updates the entry with the new_name
"""
def test_update_name_updates_entry_with_new_name():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    birthdays.update_name("Char","Jon")
    assert birthdays.manager["Jon"] == "1993-11-17"

"""
Given a name that doesn't exist in manager:
It throws an Exception => "No friend with that name"
"""
def test_update_name_raise_exception_when_name_not_found():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    with pytest.raises(Exception) as error:
        birthdays.update_name("Jon", "Char")
    error_message = str(error.value)
    assert error_message == "No friend with that name"

"""   
Given an empty string for new_name
raises an exception => "Name cannot be empty string!"
"""
def test_update_name_with_empty_string_for_new_nameraises_an_exception():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1993-11-17")
    with pytest.raises(Exception) as error:
        birthdays.update_name("Char", "")
    error_message = str(error.value)
    assert error_message == "new_name cannot be empty string!"


def test_dob_string_converter():
        birthdays = BirthdayManager()
        assert isinstance(birthdays._dob_string_converter("1993-11-17"), datetime)
        assert birthdays._dob_string_converter("1993-11-17").month == 11
        assert birthdays._dob_string_converter("1993-11-17").day == 17

def test__dob_dt_converter():
        birthdays = BirthdayManager()
        assert isinstance(birthdays._dob_dt_converter(datetime(1990, 6, 19, 0, 0)), str)
        assert birthdays._dob_dt_converter(datetime(1990, 6, 29, 0, 0)) == "1990-06-29"


"""   
When called
upcoming_birthdays returns a list of friends with birthdays this month and next month
"""
def test_upcoming_birthdays_returns_list_of_upcoming_birthdays():
    birthdays = BirthdayManager()
    birthdays.add("Char", "1990-06-19") # This month
    birthdays.add("Abby", "1993-07-20") # Next month
    birthdays.add("Adam", "1993-08-28") # N/A
    birthdays.add("Jon", "1996-01-18") # N/A
    assert type(birthdays.upcoming_birthdays()) == list
    assert birthdays.upcoming_birthdays() == [{"Char": "1990-06-19"}, {"Abby":"1993-07-20"}]
    birthdays.add("Jon", "1996-07-01") # Next month
    assert birthdays.upcoming_birthdays() == [{"Char": "1990-06-19"}, {"Abby":"1993-07-20"}, {"Jon": "1996-07-01"}]








