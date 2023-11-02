def solution():
    parking_time = 5
    walking_time = 3
    metal_detector_crowded_time = 30
    metal_detector_not_crowded_time = 10
    work_days = 5

    # Calculate the total time spent parking and walking into the courthouse each day
    daily_parking_time = parking_time + walking_time

    # Calculate the total time spent at the metal detector for crowded and not crowded days
    total_crowded_time = metal_detector_crowded_time * 2
    total_not_crowded_time = metal_detector_not_crowded_time * 3

    # Calculate the total time spent on all activities each day
    daily_total_time = daily_parking_time + total_crowded_time + total_not_crowded_time

    # Calculate the total time spent on all activities in a week
    weekly_total_time = daily_total_time * work_days
    result = weekly_total_time
    return result

print(solution())