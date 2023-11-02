def solution():
    # Define times for parking and walking
    parking_time = 5
    walking_time = 3

    # Calculate time spent on metal detectors
    crowded_days_time = 2 * 30
    less_crowded_days_time = 3 * 10
    metal_detector_time = crowded_days_time + less_crowded_days_time

    # Calculate total time spent on all activities in a week
    work_days = 5
    total_time = (parking_time + walking_time + metal_detector_time) * work_days
    result = total_time
    return result

print(solution())