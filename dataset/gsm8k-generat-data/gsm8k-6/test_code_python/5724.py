def solution():
    # Calculate the distance Jason needs to cover after driving for 30 minutes
    distance_left = 120 - (60 * 0.5)  # Jason has already covered 30 miles by driving at 60 mph for 30 minutes

    # Calculate the speed Jason needs to average for the remainder of the drive
    time_left = 1.5 - 0.5  # Jason has already driven for 30 minutes
    speed_needed = distance_left / time_left

    result = speed_needed
    return result

print(solution())