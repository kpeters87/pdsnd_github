import pandas as pd
import time

import functions as fc
import user_stats as usta

print("Hello Welcome to BikeShare data")
# list the cites to make easy to avoid typing error
cites = ['Chicago', 'New York City', 'Washington']
# Call a list to show the selection and keep to avoid problems
test = ''
while test != 'q':
    while True:  # This loop make sure that the dataframe is not empty
        #  call function to help the selection of cites month e days
        user_city = fc.user_sections('cities')
        user_month = fc.user_sections('month')
        user_day = fc.user_sections('days')
        df = fc.city(user_city)
        df = fc.filter(df, user_month, user_day)
        if isinstance(df, pd.DataFrame):
            break
        else:
            print(df)
    start_time = time.time()
    fc.popular_time(df)
    fc.station_stats(df)
    fc.trip_duration_stats(df,user_month, user_day)
    usta.user_stats(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    test = input("Press q to exit, or something else to explore again:")
    print("Thank you!")