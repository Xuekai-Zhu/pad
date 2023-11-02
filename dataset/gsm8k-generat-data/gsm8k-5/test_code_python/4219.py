def solution():
    beats_per_minute = 200  # James listens to music with 200 beats per minute
    minutes_per_hour = 60  # There are 60 minutes in an hour
    hours_per_day = 2  # James listens to music for 2 hours per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of beats James hears per week
    total_beats = beats_per_minute * minutes_per_hour * hours_per_day * days_per_week

    result = total_beats
    return result

print(solution())