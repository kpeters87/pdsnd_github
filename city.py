import pandas as pd
import datetime
#Code responsible to recive the number assingned to each city and return a dataframe to the main code
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
if __name__ == "__main__":
    city('Chicago')