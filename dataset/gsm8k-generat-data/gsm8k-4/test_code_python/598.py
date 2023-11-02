def solution():
    """Federal guidelines recommend eating at least 2 cups of vegetables per day. From breakfast on Sunday to the end of the day on Thursday, Sarah has eaten 8 cups. How many cups per day does Sarah need to eat of her vegetables in order to meet her daily minimum requirement for the week?"""
    # Define the minimum cups of vegetables per day
    MINIMUM_VEGETABLES_PER_DAY = 2

    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Define the number of cups of vegetables Sarah has already eaten
    cups_eaten = 8

    # Calculate the remaining number of cups of vegetables Sarah needs to eat
    cups_remaining = (MINIMUM_VEGETABLES_PER_DAY * DAYS_IN_WEEK) - cups_eaten

    # Calculate the number of cups of vegetables Sarah needs to eat per day to meet her daily minimum requirement for the week
    cups_per_day = cups_remaining / (DAYS_IN_WEEK - 5)

    # Return the result
    result = cups_per_day
    return result

print(solution())