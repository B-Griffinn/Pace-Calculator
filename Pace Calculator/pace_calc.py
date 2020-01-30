# Pace Calculator

def pace_calc():
    # Store a users input so we can run the proper calculations to retrieve thier pace
    distance_type = str(input('Enter your prefered distance type: km or mi only. ')).lower()

    # conditonally check if the user entered km
    if distance_type == 'km':
        # prompt the user for the number of hours and convert into seconds and update time
        time = 3600 * int(input('Please enter the number of hours you ran: '))
        # prompt the user for the number of minutes and covert into seconds and update time
        time = time + 60 * int(input('Please enter the number of minutes you ran: '))
        # prompt the user for the number of seconds and update time
        time = time + int(input('Please enter how many seconds you ran: '))
        # prompt user for their ditance and convert into a float
        distance = float(input('Please enter the distance you ran: '))

        # calculate the pace with users input
        pace = int(time / distance)

        # use the divmod in order to return pace in minutes and seconds
        mm, ss = divmod(pace, 60)

        # return mm:ss along with a message "your pace was..."
        return f"You ran {distance}km's at a pace of {mm}:{ss}"
    # conditonally check if the user entered km
    elif distance_type == 'mi':
        # prompt the user for the number of hours and convert into seconds and update time
        time = 3600 * int(input('Please enter the number of hours you ran: '))
        # prompt the user for the number of minutes and covert into seconds and update time
        time = time + 60 * int(input('Please enter the number of minutes you ran: '))
        # prompt the user for the number of seconds and update time
        time = time + int(input('Please enter how many seconds you ran: '))
        # prompt user for their ditance and convert into a float
        distance = float(input('Please enter the distance you ran: '))

        # calculate the pace with users input
        pace = int(time / distance)

        # use the divmod in order to return pace in minutes and seconds
        mm, ss = divmod(pace, 60)

        # return mm:ss along with a message "your pace was..."
        return f"You ran {distance}mi's at a pace of {mm}:{ss}"


print(pace_calc())