def solution():
    """Kelly booked a three week vacation to visit relatives.  The first day, she spent traveling.  The next 5 days she spent at her Grandparents' house.  The next day, she spent traveling.  Then, she spends the next 5 days at her brother's house.  Then she spent two days traveling to her sister's house, spent several days at her sister's house, and then spent two more days traveling home.  How many days did she spend at her sister's house?"""
    # Define the number of days for each portion of the vacation
    travel_day = 1
    grandparents_day = 5
    brother_day = 5
    sister_travel = 2
    sister_total = 0 # initialize sister_total
    sister_stay = 0 # initialize sister_stay
    sister_travel_home = 2

    # Calculate the total number of days of the vacation
    total_days = travel_day + grandparents_day + travel_day + brother_day + sister_travel + sister_total + sister_travel_home

    # Calculate the number of days spent at sister's house
    sister_stay = total_days - (travel_day*3 + grandparents_day + brother_day + sister_travel + sister_travel_home)
    result = sister_stay
    return result

print(solution())