def solution():
    # Convert 4 minutes to seconds
    time_in_seconds = 4 * 60

    # Calculate the number of car collisions in the given time
    car_collisions = time_in_seconds // 10

    # Calculate the number of big crashes in the given time
    big_crashes = time_in_seconds // 20

    # Calculate the total number of accidents
    total_accidents = car_collisions + big_crashes
    result = total_accidents
    return result

print(solution())