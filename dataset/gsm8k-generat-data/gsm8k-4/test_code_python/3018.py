def solution():
    """Kara has to drink 4 ounces of water every time she takes her medication. Her medication instructions are to take one tablet three times a day. She followed the instructions for one week, but in the second week, she forgot twice on one day. How many ounces of water did she drink with her medication over those two weeks?"""
    # Define the number of tablets taken each day and the number of days in each week
    tablets_per_day = 3
    days_per_week = 7

    # Calculate the total number of tablets taken in one week
    tablets_per_week = tablets_per_day * days_per_week

    # Calculate the total amount of water drank in one week
    water_per_week = tablets_per_week * 4

    # Calculate the number of tablets missed in the second week
    tablets_missed = 2 * tablets_per_day

    # Calculate the total number of tablets taken in the second week
    tablets_second_week = tablets_per_week - tablets_missed

    # Calculate the total amount of water drank in two weeks
    water_total = (water_per_week * 2) - (tablets_missed * 4)

    # return the result
    result = water_total
    return result

print(solution())