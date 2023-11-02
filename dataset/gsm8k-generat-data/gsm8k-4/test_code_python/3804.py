def solution():
    """Corveus sleeps 4 hours a day and his doctor recommended for him to sleep 6 hours a day. How many hours of sleep does Corveus lack in a week?"""
    # Define the number of hours Corveus sleeps and the recommended number of hours
    hours_sleep = 4
    hours_recommend = 6

    # Calculate the number of hours Corveus lacks each day
    hours_lack = hours_recommend - hours_sleep

    # Calculate the number of hours Corveus lacks in a week
    hours_lack_week = hours_lack * 7

    # return the result
    result = hours_lack_week
    return result

print(solution())