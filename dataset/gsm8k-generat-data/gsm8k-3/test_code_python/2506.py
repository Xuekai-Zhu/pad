def solution():
    """Tom has only been getting 6 hours of sleep a day.  He increases that by 1/3.  How many hours of sleep does he get per night?"""
    # Define Tom's current daily sleep hours and the increase
    CURRENT_SLEEP = 6
    INCREASE = 1/3

    # Calculate Tom's new daily sleep hours
    new_sleep = CURRENT_SLEEP + (CURRENT_SLEEP * INCREASE)

    # Display Tom's new daily sleep hours
    result = new_sleep
    return result

print(solution())