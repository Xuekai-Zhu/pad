def solution():
    """James listens to super-fast music. It is 200 beats per minute. He listens to 2 hours of music a day. How many beats does he hear per week?"""
    # Define the beats per minute and the listening time in minutes per day
    BEATS_PER_MINUTE = 200
    MINUTES_PER_DAY = 120

    # Calculate the beats heard per day and per week
    beats_per_day = BEATS_PER_MINUTE * MINUTES_PER_DAY
    beats_per_week = beats_per_day * 7

    # Calculate the total beats heard in a week
    total_beats = beats_per_week * 2

    # return the result
    result = total_beats
    return result

print(solution())