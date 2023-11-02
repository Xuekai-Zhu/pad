def solution():
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_per_day = 2
    num_days = 3

    # Calculate the total number of minutes John plays over 3 days
    total_minutes = num_days * hours_per_day * minutes_per_hour

    # Calculate the total number of beats John plays over 3 days
    total_beats = total_minutes * beats_per_minute
    result = total_beats
    return result

print(solution())