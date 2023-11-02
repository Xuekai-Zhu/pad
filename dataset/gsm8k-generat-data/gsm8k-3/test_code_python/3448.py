def solution():
    """Barney washes his kitchen towels once a week. He owns eighteen towels and uses two at a time that he changes to clean towels daily. He missed one week of laundry. How many days the following week will Barney not have clean towels?"""
    # Define the number of towels Barney owns
    NUM_TOWELS = 18

    # Define the number of towels Barney uses per day
    TOWELS_PER_DAY = 2

    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Calculate the number of towels Barney uses per week
    towels_per_week = TOWELS_PER_DAY * DAYS_IN_WEEK

    # Calculate the number of weeks Barney missed washing his towels
    missed_weeks = 1

    # Calculate the number of clean towels Barney has after the missed week
    clean_towels = NUM_TOWELS - (missed_weeks * towels_per_week)

    # Calculate the number of days Barney does not have clean towels
    dirty_days = (DAYS_IN_WEEK * 2) - clean_towels

    # Display the number of days Barney does not have clean towels
    result = dirty_days
    return result

print(solution())