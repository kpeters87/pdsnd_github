
def station_stats(df):


    # display most commonly used start station df.groupby('month').size().to_frame(name='count').reset_index()
    group_start_station = df.groupby('Start Station').size().to_frame(name='count')
    print(group_start_station.sort_values('count', ascending=False).head(5).to_string())
    # display most commonly used end station
    group_end_station = df.groupby('End Station').size().to_frame(name='count')
    print(group_end_station.sort_values('count', ascending=False).head(5).to_string())
    # display most frequent combination of start station and end station trip
    group_Start_end_station = df.groupby(['Start Station', 'End Station']).size().to_frame(name='count')
    print(group_Start_end_station.sort_values('count', ascending=False).head(5).to_string())

    print('-' * 40)

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
    df = ft.filter(df, user_month,user_day)
    station_stats(df)
