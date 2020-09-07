import pandas as pd
import datetime

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def user_sections(type_of_selection):
    list_cites = ['Chicago', 'New York City', 'Washington']
    list_month = ['All month', 'Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list_days = ['All days', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    list = []

    if type_of_selection == 'cities': list = list_cites
    if type_of_selection == 'month': list = list_month
    if type_of_selection == 'days': list = list_days
    while True:  # This loop make sure that user select right
        try:
            print("SELECT THE MONTH FOLLOWING THE INSTRUCTIONS")
            for (i, item) in enumerate(list, start=0):
                print("Press {} for {}".format(i, item))
            user_choice = int(input("Your choice:"))
            test = list[user_choice]
        except ValueError:
            print("Sorry, wrong information. Try again")
            continue
        except IndexError:
            print("Please select a v1id number. Try again")
            continue
        else:
            print('-------------------')
            print("You chose: {}".format(test))
            print('-------------------')
            break  # Right Input, lets go
    return test

def city(city_index):
    """
    This function get user choosen city and retrive the dataframe.
    Args:
        (str) city_index - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data whit 3 new collums Month, Week_day and Hour
    """
    df = pd.read_csv(CITY_DATA[city_index])
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['week_day'] = pd.DatetimeIndex(df['Start Time']).weekday
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    return df

def filter(df, month, day):
    """
    This functions get the info provided about filtering data from user and set the dataframe filtered at the end
    Args:
    (DataFrame) df - dataframe provided from cities function
    (str) month - Month name with first three words or All month.
    (str) day - Week day full name or All Days.
    Returns:
    (df) Pandas DataFrame - DataFrame filtered with choosen data from user
    """
    list_month = ['All month', 'Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list_days = ['All days', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    s_month = list_month.index(month)
    s_day = list_days.index(day)
    # filter by month where 0 is all month

    if s_month != 0:
        df = df[(pd.DatetimeIndex(df['Start Time']).month == s_month)]
        if df.empty == True:
            return "No data to the this combination of day and month, try again"
    #filter by day where 0 is all days

    if s_day != 0:
        df = df[(pd.DatetimeIndex(df['Start Time']).weekday == s_day)]
        if df.empty == True:
            return "No data to the this combination of day and month, try again"
    return df