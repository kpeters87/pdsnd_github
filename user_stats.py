

def user_stats(df):
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


if __name__ == "__main__":
    import pandas as pd
    desired_width = 320
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', 20)

    import city as ct
    import filter as ft
    import user_selections as usel
    user_month = 'All month'
    user_day = 'All days'
    user_city = 'Chicago'
    # Washington
    # Chicago

    df = ct.city(user_city)
    df = ft.filter(df, user_month, user_day)
    user_stats(df)