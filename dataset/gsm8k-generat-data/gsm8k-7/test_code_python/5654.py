def solution():
    minutes_per_weekday = 15
    minutes_per_weekend = minutes_per_weekday * 2
    num_weekdays = 5
    num_weekends = 2

    # Calculate the total minutes Daniel practices during the weekdays
    total_weekday_minutes = minutes_per_weekday * num_weekdays

    # Calculate the total minutes Daniel practices during the weekends
    total_weekend_minutes = minutes_per_weekend * num_weekends

    # Calculate the total minutes Daniel practices during the whole week
    total_minutes = total_weekday_minutes + total_weekend_minutes
    result = total_minutes
    return result

print(solution())