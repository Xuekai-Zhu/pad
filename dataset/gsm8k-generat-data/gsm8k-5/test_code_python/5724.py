def solution():
    total_distance = 120  # Jason has to drive 120 miles
    first_half_distance = total_distance / 2  # Jason drives 60 miles for the first 30 minutes
    second_half_distance = total_distance - first_half_distance  # Jason has to drive the remaining distance

    # Calculate the time Jason has to complete the second half of the drive
    time_remaining = 1.5 - 0.5  # Jason has already driven for 30 mins, and he has 1.5 hours in total

    # Calculate the required speed to complete the second half of the drive on time
    required_speed = second_half_distance / time_remaining
    result = required_speed
    return result

print(solution())