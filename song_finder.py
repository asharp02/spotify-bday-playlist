from datetime import datetime

""" File that reads in a date from the command line and 
finds the top song on that day for all years since that date"""

# Grab date from input
def grab_birthday():
    # prompts a user for their birthday in the form of MMDDYYYY
    invalid_input = True
    bday = None
    while invalid_input:
        invalid_input = False
        bday_raw = input("Please enter your birthday (MMDDYYYY): ")
        if len(bday_raw) > 8 or len(bday_raw) < 8:
            invalid_input = True
            print("Must input 8 characters!")
            print()
            continue
        try:
            month = int(bday_raw[:2])
            date = int(bday_raw[2:4])
            year = int(bday_raw[4:])
            bday = datetime(month=month, day=date, year=year)
        except (TypeError, ValueError):
            invalid_input = True
            print("Invalid Input, Birthday format must be MMDDYYYY")
            print()
            continue


# Iterate through all years since that date and query billboard for the #1 song on that date

