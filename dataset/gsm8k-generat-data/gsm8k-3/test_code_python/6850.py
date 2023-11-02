def solution():
    """Dave breaks 2 guitar strings per night when playing live.  If he performs 6 shows a week for 12 weeks, how many guitar strings will he need to replace?"""
    # Define the number of strings Dave breaks per show
    STRINGS_PER_SHOW = 2

    # Define the number of shows Dave performs per week and per 12-week period
    SHOWS_PER_WEEK = 6
    SHOWS_PER_PERIOD = 12

    # Calculate the total number of shows Dave performs
    total_shows = SHOWS_PER_WEEK * SHOWS_PER_PERIOD

    # Calculate the total number of strings Dave needs to replace
    total_strings = STRINGS_PER_SHOW * total_shows

    # Display the total number of strings
    result = total_strings
    return result

print(solution())