def solution():
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_per_day = 2
    days_per_week = 7

    # Calculate the total minutes per week
    total_minutes = minutes_per_hour * hours_per_day * days_per_week

    # Calculate the total beats per week
    total_beats = beats_per_minute * total_minutes
    result = total_beats
    return result

print(solution())