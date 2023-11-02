def solution():
    """James listens to super-fast music.  It is 200 beats per minute.  He listens to 2 hours of music a day.  How many beats does he hear per week?"""
    # Define the beats per minute and the hours of music listened per day
    BEATS_PER_MINUTE = 200
    HOURS_PER_DAY = 2

    # Calculate the beats heard in one day
    beats_per_day = BEATS_PER_MINUTE * 60 * HOURS_PER_DAY

    # Calculate the beats heard in one week
    beats_per_week = beats_per_day * 7

    # Display the total beats heard per week
    result = beats_per_week
    return result

print(solution())