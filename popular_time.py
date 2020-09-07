def popular_time(df):
    list_month = ['All month', 'Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
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
    popular_time(df)