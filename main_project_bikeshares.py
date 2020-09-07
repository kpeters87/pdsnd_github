import pandas as pd
import time

import functions as fc

print("Hello Welcome to BikeShare data")
# list the cites in that way the user doesn't need to type it.
cites = ['Chicago', 'New York City', 'Washington']
# Call a list to show the selection and keep to avoid problems
test = ''
while test != 'q':
    while True:  # This loop make sure that the dataframe is not empty
        #  call function to help the selection of cites month e days
        user_city = fc.user_sections('cities')
        user_month = fc.user_sections('month')
        user_day = fc.user_sections('days')
        user_raw = fc.user_sections('raw')
        df = fc.city(user_city)
        df = fc.filter(df, user_month, user_day)
        if isinstance(df, pd.DataFrame):
            break
        else:
            print(df)
    start_time = time.time()
    if user_raw == 'Yes':
        while True:
            try:
                lines= int(input("How many lines: "))
            except ValueError:
                print("Sorry, give a integer number")
                continue
            else:
                break
        print(df.head(lines))
    else:
        fc.popular_time(df)
        fc.station_stats(df)
        fc.trip_duration_stats(df,user_month, user_day)
        fc.user_stats(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    test = input("Press q to exit, or something else to explore again:")
    print("Thank you!")