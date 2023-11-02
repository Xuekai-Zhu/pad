def solution():
    # Calculate the total time Mark spends on parking and walking into the courthouse
    parking_time = 5  # minutes
    walking_time = 3  # minutes
    total_time = (parking_time + walking_time) * 5  # 5 work days in a week

    # Calculate the time it takes Mark to get through the metal detector on 2 days of the week
    metal_detector_time = 30 * 2  # minutes

    # Calculate the time it takes Mark to get through the metal detector on 3 days of the week
    metal_detector_time_less_crowded = 10 * 3  # minutes

    # Calculate the total time Mark spends on all activities in a week
    total_time += metal_detector_time + metal_detector_time_less_crowded
    result = total_time
    return result

print(solution())