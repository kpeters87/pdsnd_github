import pandas as pd
import time

import city as ct
import filter as ft
import user_selections as usel
import popular_time as pt
import station_stats as st
import trip_duration as td
import user_stats as usta

print("Hello Welcome to BikeShare data")
# list the cites to make easy to avoid typing error
cites = ['Chicago', 'New York City', 'Washington']
# Call a list to show the selection and keep to avoid problems
test = ''
while test != 'q':
    while True:  # This loop make sure that the dataframe is not empty
        #  call function to help the selection of cites month e days
        user_city = usel.user_sections('cities')
        user_month = usel.user_sections('month')
        user_day = usel.user_sections('days')
        df = ct.city(user_city)
        df = ft.filter(df, user_month, user_day)
        if isinstance(df, pd.DataFrame):
            break
        else:
            print(df)
    start_time = time.time()
    pt.popular_time(df)
    st.station_stats(df)
    td.trip_duration_stats(df,user_month, user_day)
    usta.user_stats(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    test = input("Press q to exit, or something else to explore again:")
    print("Thank you!")