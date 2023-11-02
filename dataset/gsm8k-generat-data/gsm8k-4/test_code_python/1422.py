def solution():
    """Every 10 seconds, there is a car collision, and every 20 seconds there is a big crash. How many accidents overall will happen in 4 minutes?"""
    # Define the time period in seconds
    time_period = 4 * 60

    # Calculate the frequency of car collisions per second
    car_collision_freq = 1 / 10

    # Calculate the frequency of big crashes per second
    big_crash_freq = 1 / 20

    # Calculate the total number of car collisions
    car_collisions = car_collision_freq * time_period

    # Calculate the total number of big crashes
    big_crashes = big_crash_freq * time_period

    # Calculate the total number of accidents
    total_accidents = car_collisions + big_crashes

    # Return the result
    result = total_accidents
    return result

print(solution())