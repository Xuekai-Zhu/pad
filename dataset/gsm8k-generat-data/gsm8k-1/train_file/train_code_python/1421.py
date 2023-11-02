def solution():
    """Every 10 seconds, there is a car collision, and every 20 seconds there is a big crash. How many accidents overall will happen in 4 minutes?"""
    car_collision_freq = 10
    big_crash_freq = 20

    # Convert 4 minutes to seconds
    time_in_seconds = 4 * 60

    # Calculate the number of car collisions during the time period
    car_collision_count = time_in_seconds // car_collision_freq

    # Calculate the number of big crashes during the time period
    big_crash_count = time_in_seconds // big_crash_freq

    # Calculate the total number of accidents
    total_accidents = car_collision_count + big_crash_count

    result = total_accidents
    return result

print(solution())