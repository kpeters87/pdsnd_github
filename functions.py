import pandas as pd
import datetime

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

list_month = ['All month', 'Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def user_sections(type_of_selection):
    """
    This function is responsible to catch what the user want to pass to the next functions
    Args:
    (str) type_of_selection - This functions ask the user adpting to 3 types os inputs: cities, month, days and raw
                              each one gets the proper list and provide questions to user
    Return:
    (str) test - The result of the test of the question to user, if its valid it passes as resultf from function
    """

    list_cites = ['Chicago', 'New York City', 'Washington']

    list_days = ['All days', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    list_raw = ['Yes', 'No']
    list = []

    if type_of_selection == 'cities': 
        list = list_cites
        text = "SELECT THE CITY FOLLOWING THE INSTRUCTIONS"
    if type_of_selection == 'month': 
        list = list_month
        text = "SELECT THE MONTH FOLLOWING THE INSTRUCTIONS"
    if type_of_selection == 'days': 
        list = list_days
        text = "SELECT THE WEEK DAY FOLLOWING THE INSTRUCTIONS"
    if type_of_selection == 'raw': 
        list = list_raw
        text = "DISPLAY RAW DATA?"
    while True:  # This loop make sure that user select right
        try:
            print(text)
            for (i, item) in enumerate(list, start=0):
                print("Press {} for {}".format(i, item))
            user_choice = int(input("Your choice:"))
            test = list[user_choice]
        except ValueError:
            print("Sorry, wrong information. Try again")
            continue
        except IndexError:
            print("Please select a valid number. Try again")
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

def popular_time(df):
    """
    This functions get the filtered dataframe and print the desired questions
    Args:
    (DataFrame) df - dataframe provided with cities, days and month filtered
    
    Returns:
    Prints to user: display the most common month, 
                    display the most common day of week and 
                    display the most common start hour
    """
    list_month_dict = dict(enumerate(list_month))
    list_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    list_days_dict = dict(enumerate(list_days))

    # display the most common month
    group_month = df.groupby('month').size().to_frame(name='count').reset_index()
    group_month['month'] = group_month['month'].map(list_month_dict)
    group_month.set_index('month',inplace=True)
    print(group_month.sort_values('count',ascending=False).head(5).to_string())

    # display the most common day of week
    group_week_day = df.groupby('week_day').size().to_frame(name='count').reset_index()
    group_week_day['week_day'] = group_week_day['week_day'].map(list_days_dict)
    group_week_day.set_index('week_day',inplace=True)
    print(group_week_day.sort_values('count',ascending=False).head(5).to_string())

    # display the most common start hour
    group_hour = df.groupby('hour').size().to_frame(name='count').reset_index()
    group_hour.set_index('hour')
    group_hour.set_index('hour',inplace=True)
    print(group_hour.sort_values('count',ascending=False).head(5).to_string())

def station_stats(df):

    """
    This functions get the filtered dataframe and print the desired questions
    Args:
    (DataFrame) df - dataframe provided with cities, days and month filtered
    
    Returns:
    Prints to user: display most commonly used start station,
                    display most commonly used
                    and station and display most frequent combination of start station and end station trip
    """
    # display most commonly used start station
    group_start_station = df.groupby('Start Station').size().to_frame(name='count')
    print(group_start_station.sort_values('count', ascending=False).head(5).to_string())
    # display most commonly used end station
    group_end_station = df.groupby('End Station').size().to_frame(name='count')
    print(group_end_station.sort_values('count', ascending=False).head(5).to_string())
    # display most frequent combination of start station and end station trip
    group_Start_end_station = df.groupby(['Start Station', 'End Station']).size().to_frame(name='count')
    print(group_Start_end_station.sort_values('count', ascending=False).head(5).to_string())

    print('-' * 40)

def trip_duration_stats(df, user_month, user_day):
    """
    This functions get the filtered dataframe and print the desired questions
    Args:
    (DataFrame) df - dataframe provided with cities, days and month filtered
    (str)user_month = receive the provided user month to fill the string
    (str)user_day = receive the provided user week day to fill the string
    
    Returns:
    Prints to user: display total travel time
                    display mean travel time
    """
    # display total travel time
    df['Time Difference'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    print("The total travel time for {}, selecting {} is: {}".format(user_month, user_day, df['Time Difference'].sum()))
    print('-' * 20)

    # display mean travel time
    print("The mean travel time for {}, selecting {} is: {}".format(user_month, user_day, str(df['Time Difference'].mean()).split(".")[0]))
    print('-'*40)

def user_stats(df):
    """
    This functions get the filtered dataframe and print the desired questions
    Args:
    (DataFrame) df - dataframe provided with cities, days and month filtered
    
    Returns:
    Prints to user: Display counts of user types,
                    Display counts of gender
                    Display earliest, most recent, and most common year of birth
    """
    if __name__ == "__main__":
        print(df)
        print(df['User Type'].isnull().sum())
    # Display counts of user types
    group_user_type = df.groupby('User Type').size().to_frame(name='count')
    print(group_user_type)
    print('-' * 20)

    # Display counts of gender
    if 'Gender' in df:
        group_user_gender = df.groupby('Gender').size().to_frame(name='count')
        print(group_user_gender)
        print('-' * 20)
    # Display earliest, most recent, and most common year of birth
        print("The oldest person was born in: {}".format(int(df['Birth Year'].max())))
        print("The youngest person was born in: {}".format(int(df['Birth Year'].min())))
        print("The most common year of birth is: {}".format(int(df['Birth Year'].mode())))
    print('-' * 40)