import pandas as pd

def trip_duration_stats(df, user_month, user_day):

    # display total travel time
    df['Time Difference'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    print("The total travel time for {}, selecting {} is: {}".format(user_month, user_day, df['Time Difference'].sum()))
    print('-' * 20)
    # display mean travel time

    print("The mean travel time for {}, selecting {} is: {}".format(user_month, user_day, str(df['Time Difference'].mean()).split(".")[0]))

    print('-'*40)

if __name__ == "__main__":
    import pandas as pd
    desired_width = 320
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 20)

    import city as ct
    import filter as ft
    import user_selections as usel

    df = ct.city('Chicago')
    # user_month = usel.user_sections('month')
    # user_day = usel.user_sections('days')
    user_month = 'All month'
    user_day = 'All days'
    df = ft.filter(df, user_month, user_day)
    trip_duration_stats(df, user_month, user_day)
