import pandas as pd
import datetime

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
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