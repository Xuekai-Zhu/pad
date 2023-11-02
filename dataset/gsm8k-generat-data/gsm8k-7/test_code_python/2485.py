def solution():
    butterfly_hours_per_day = 3
    butterfly_days_per_week = 4

    backstroke_hours_per_day = 2
    backstroke_days_per_week = 6

    num_weeks = 4

    # Calculate the total number of hours spent on butterfly stroke
    butterfly_total_hours = butterfly_hours_per_day * butterfly_days_per_week * num_weeks

    # Calculate the total number of hours spent on backstroke
    backstroke_total_hours = backstroke_hours_per_day * backstroke_days_per_week * num_weeks

    # Calculate the total time spent practicing swimming
    total_hours = butterfly_total_hours + backstroke_total_hours
    result = total_hours
    return result

print(solution())