# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class BirthdayManager:
    # User-facing properties:
    #   name: string
    #   birthday: string (YYYY-MM-DD)

    def __init__(self):
        self.manager = {}
        # Parameters:
        #   None
        # Side effects:
        #   None

        pass # No code here yet

    def add(self, name, dob)
        # Parameters:
        #   name: string representing a friend's name
        #   dob:  string representing a friend's dob (YYY-MM-DD)
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the friend's birthday to the self object
        #   Throws exception if name is an empty string
        #   Throws exception if dob is in incorrect format

        pass # No code here yet

    def update_birthday(self, name, new_date)
         # Parameters:
        #   name: string representing a friend's name
        #   new_date:  string representing a friend's updated dob (YYY-MM-DD)
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the friend's birthday with the new birthday date to the self object
        #   Throws exception if name doesn't exist in Birthday Manager

        pass # No code here yet

    def update_name(self, name, new_name)
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
        #   List of friends + birthdays for the birthdays coming up this month and next month
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
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
