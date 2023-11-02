def solution():
    weekday_practice_time = 30 # in minutes
    saturday_practice_time = weekday_practice_time * 3
    num_weekdays = 5
    num_weekend_days = 2

    # Calculate the total practice time on weekdays
    total_weekday_practice_time = weekday_practice_time * num_weekdays

    # Calculate the total practice time on Saturday
    total_saturday_practice_time = saturday_practice_time * num_weekend_days

    # Calculate the total practice time for the week in minutes
    total_practice_time = total_weekday_practice_time + total_saturday_practice_time

    # Convert total practice time from minutes to hours
    total_practice_time_hours = total_practice_time / 60
    result = total_practice_time_hours
    return result

print(solution())