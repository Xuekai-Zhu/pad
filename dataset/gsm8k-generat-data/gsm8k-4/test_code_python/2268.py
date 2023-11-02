def solution():
    """Kevin has a shoebox filled with toads. Every day, Kevin feeds each toad 3 worms. It takes Kevin 15 minutes to find each worm. If it takes Kevin 6 hours to find enough worms to feed all of his toads, how many toads does Kevin have in his shoebox?"""
    # Define the time it takes to find one worm
    WORM_TIME = 15  # minutes

    # Define the time Kevin spends finding worms each day
    daily_worm_time = 6 * 60  # 6 hours in minutes

    # Calculate the number of worms Kevin can find each day
    worms_per_day = daily_worm_time / WORM_TIME

    # Calculate the number of toads Kevin has based on the number of worms he can feed each day (assuming he feeds them all every day)
    toads = worms_per_day / 3

    # return the result
    result = toads
    return result

print(solution())