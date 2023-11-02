def solution():
    time_pickup = 5
    time_vacuum = 20
    time_clean_windows = 15
    time_dust_furniture = 10
    num_weeks = 4

    # Calculate the total time spent cleaning the living room each week
    total_time_weekly = time_pickup + time_vacuum + time_clean_windows + time_dust_furniture

    # Calculate the total time spent cleaning the living room over 4 weeks
    total_time = total_time_weekly * num_weeks
    result = total_time
    return result

print(solution())