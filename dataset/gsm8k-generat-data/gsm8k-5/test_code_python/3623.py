def solution():
    parking_time = 5  # Mark spends 5 minutes finding parking
    walking_time = 3  # Mark spends 3 minutes walking to the courthouse
    metal_detector_slow_days = 3  # Mark has 3 days where the metal detector takes 10 minutes
    metal_detector_busy_days = 2  # Mark has 2 days where the metal detector takes 30 minutes
    work_days = 5  # Mark works 5 days a week

    # Calculate the total time Mark spends parking and walking to the courthouse
    parking_and_walking_time = (parking_time + walking_time) * work_days

    # Calculate the total time Mark spends at the metal detector on slow days
    slow_detector_time = 10 * metal_detector_slow_days

    # Calculate the total time Mark spends at the metal detector on busy days
    busy_detector_time = 30 * metal_detector_busy_days

    # Calculate the total time Mark spends on all these activities in a week
    total_time = parking_and_walking_time + slow_detector_time + busy_detector_time
    result = total_time
    return result

print(solution())