def solution():
    # Define the number of trains and carriages
    num_trains = 4
    num_carriages = 4

    # Calculate the number of wheels in each carriage
    num_wheels_per_carriage = 3 * 5

    # Calculate the total number of wheels
    total_wheels = num_trains * num_carriages * num_wheels_per_carriage

    result = total_wheels
    return result

print(solution())