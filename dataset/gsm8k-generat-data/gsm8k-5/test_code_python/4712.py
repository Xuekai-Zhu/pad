def solution():
    distance_walked = 3  # Tony walks 3 miles every morning with the backpack
    distance_run = 10  # Tony runs 10 miles every morning without the backpack
    time_walked = distance_walked / 3  # It takes Tony 1 hour to walk 3 miles at 3 miles per hour
    time_run = distance_run / 5  # It takes Tony 2 hours to run 10 miles at 5 miles per hour
    total_time = time_walked + time_run  # Tony spends this much time exercising every morning
    days_per_week = 7  # Tony exercises every morning, 7 days per week

    # Calculate the total number of hours Tony spends exercising each week
    total_hours = total_time * days_per_week
    result = total_hours
    return result

print(solution())