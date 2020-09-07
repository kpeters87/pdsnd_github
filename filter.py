import pandas as pd
import city as ct

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

if __name__ == "__main__":
    desired_width = 320
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 20)
    head_size = 3
    df = ct.city("Chicago")
    df = filter(df, 'All month', 'All days' )
    print(df)

    df = ct.city("New York City")
    df = filter(df, 'Jan', 'Sunday')
    print(df.head(head_size))
    #
    # df = ct.city(3)
    # df = filter(df, 3, 2 )
    # print(df.head(head_size))