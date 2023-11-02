def solution():
    """James listens to super-fast music. It is 200 beats per minute. He listens to 2 hours of music a day. How many beats does he hear per week?"""
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_per_day = 2
    days_per_week = 7
    total_minutes = minutes_per_hour * hours_per_day * days_per_week
    total_beats = beats_per_minute * total_minutes
    result = total_beats
    return result

print(solution())