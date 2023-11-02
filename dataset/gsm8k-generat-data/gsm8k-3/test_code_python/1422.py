def solution():
    """Every 10 seconds, there is a car collision, and every 20 seconds there is a big crash. How many accidents overall will happen in 4 minutes?"""
    # Calculate the number of car collisions in 4 minutes
    car_collisions = (4 * 60) // 10

    # Calculate the number of big crashes in 4 minutes
    big_crashes = (4 * 60) // 20

    # Calculate the total number of accidents
    total_accidents = car_collisions + big_crashes

    # Display the total number of accidents
    result = total_accidents
    return result

print(solution())