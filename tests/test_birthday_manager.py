from lib.birthday_manager import BirthdayManager
import pytest

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
def test_empty_string_raises_an_exception():
    birthdays = BirthdayManager()
    with pytest.raises(Exception) as error:
        birthdays.add("", "1993-11-17")
    error_message = str(error.value)
    assert error_message == "Name cannot be empty string!"

"""
Given a name and an incorrectly-formatted DOB
raises an exception => "Warning! DOB format incorrect!"
"""
def test_incorrectly_formatted_string_raises_an_exception():
    birthdays = BirthdayManager()
    with pytest.raises(Exception) as error:
        birthdays.add("Jon", "19760911")
    error_message = str(error.value)
    assert error_message == "Warning! DOB format incorrect!"



"""
Given a name and no task
#remind raises an exception
"""
# reminder = Reminder("Kay")
# reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
# reminder = Reminder("Kay")
# reminder.remind_me_to("")
# reminder.remind() # => ", Kay!"