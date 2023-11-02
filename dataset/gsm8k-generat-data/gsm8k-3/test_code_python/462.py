def solution():
    """Roberto can skip 4,200 times an hour. Valerie can skip 80 times a minute. If they jump rope for fifteen minutes straight, how many skips will they total?"""
    # Define the number of skips per hour for Roberto and per minute for Valerie
    ROBERTO_SKIPS_PER_HOUR = 4200
    VALERIE_SKIPS_PER_MINUTE = 80

    # Get the number of minutes they jump rope
    minutes_jumped = 15

    # Calculate the total number of skips for Roberto and Valerie
    roberto_skips = ROBERTO_SKIPS_PER_HOUR / 60 * minutes_jumped
    valerie_skips = VALERIE_SKIPS_PER_MINUTE * minutes_jumped

    # Calculate the total number of skips
    total_skips = roberto_skips + valerie_skips

    # Display the total number of skips
    result = total_skips
    return result

print(solution())