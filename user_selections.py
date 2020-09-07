def user_sections(type_of_selection):
    list_cites = ['Chicago', 'New York City', 'Washington']
    list_month = ['All month', 'Jan', 'Fev', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list_days = ['All days', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    list = []

    if type_of_selection == 'cities': list = list_cites
    if type_of_selection == 'month': list = list_month
    if type_of_selection == 'days': list = list_days
    while True:  # This loop make sure that user select right
        try:
            print("SELECT THE MONTH FOLLOWING THE INSTRUCTIONS")
            for (i, item) in enumerate(list, start=0):
                print("Press {} for {}".format(i, item))
            user_choice = int(input("Your choice:"))
            test = list[user_choice]
        except ValueError:
            print("Sorry, wrong information. Try again")
            continue
        except IndexError:
            print("Please select a v1id number. Try again")
            continue
        else:
            print('-------------------')
            print("You chose: {}".format(test))
            print('-------------------')
            break  # Right Input, lets go
    return test
