def solution():
    num_floors = 10

    # Calculate the time it takes to go up to each floor
    time_per_even_floor = 15
    time_per_odd_floor = 9

    # Calculate the total time to get to the 10th floor
    total_time = 0
    for floor in range(1, num_floors + 1):
        if floor % 2 == 0:
            total_time += time_per_even_floor
        else:
            total_time += time_per_odd_floor

    # Convert the total time to minutes
    total_time_minutes = total_time / 60
    result = total_time_minutes
    return result

print(solution())