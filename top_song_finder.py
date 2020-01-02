import time
import requests

from datetime import datetime
import billboard

""" File that reads in a date from the command line and 
finds the top song on that day for all years since that date"""


def validate_input(bday_raw):
    """ Validates string passed is a valid birthday
        Returns: tuple containing (invalid_input, formatted_bday)
            where invalid_input is a boolean set to True if input is invalid
     """
    try:
        month = int(bday_raw[:2])
        date = int(bday_raw[2:4])
        year = int(bday_raw[4:])
        bday = datetime(month=month, day=date, year=year)
        if bday <= datetime.now():
            return (False, bday)
    except (TypeError, ValueError):
        return (True, None)
    return (True, None)


# Grab date from input
def grab_birthday():
    """ Prompts a user for their birthday in the form of MMDDYYYY"""
    invalid_input = True
    bday = None
    while invalid_input:
        invalid_input = False
        bday_raw = input("Please enter your birthday (MMDDYYYY): ")
        if len(bday_raw) != 8:
            invalid_input = True
            print("Must input 8 characters!")
            print()
            continue
        invalid_input, bday = validate_input(bday_raw)
        if invalid_input:
            print("Invalid Input, Birthday format must be MMDDYYYY")
            print()
            continue
    return bday


# Iterate through all years since that date and query billboard for the #1 song on that date
def get_top_songs(bday):
    top_songs = []
    for year in range(bday.year, datetime.now().year):
        date = datetime(month=bday.month, day=bday.day, year=year)
        formatted_date = date.strftime("%Y-%m-%d")
        chart = billboard.ChartData("hot-100", date=formatted_date, timeout=None)
        top_songs.append(chart[0])
    return top_songs
