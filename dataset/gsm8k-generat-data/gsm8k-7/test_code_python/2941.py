def solution():
    distance_per_day = 140
    work_days_per_week = 5
    days_off_per_week = 2  # assuming a 7-day week
    num_weeks = 4

    # Calculate the total number of work days in 4 weeks
    total_work_days = work_days_per_week * num_weeks

    # Calculate the total number of days off in 4 weeks
    total_days_off = days_off_per_week * num_weeks

    # Calculate the total distance Francine drives to work in 4 weeks
    total_distance = distance_per_day * total_work_days

    # Subtract the distance Francine does not drive on her days off
    total_distance -= distance_per_day * total_days_off

    result = total_distance
    return result

print(solution())