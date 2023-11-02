def solution():
    # Calculate the number of car collisions in 4 minutes
    car_collisions = int(4 * 60 / 10)

    # Calculate the number of big crashes in 4 minutes
    big_crashes = int(4 * 60 / 20)

    # Calculate the total number of accidents in 4 minutes
    total_accidents = car_collisions + big_crashes
    result = total_accidents
    return result

print(solution())