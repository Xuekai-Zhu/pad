def solution():
    beats_per_minute = 200  # John plays 200 beats per minute
    minutes_per_hour = 60  # There are 60 minutes in an hour
    hours_per_day = 2  # John plays 2 hours per day
    total_days = 3  # John plays for 3 days

    # Calculate the total number of beats John plays
    total_beats = beats_per_minute * minutes_per_hour * hours_per_day * total_days
    result = total_beats
    return result

print(solution())