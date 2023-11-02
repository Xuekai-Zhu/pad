def solution():
    # Calculate the time to reach each floor
    time_to_first_floor = 15
    time_to_even_floors = 15
    time_to_odd_floors = 9

    # Iterate through each floor and add up the time
    total_time = time_to_first_floor
    for floor in range(2, 11):
        if floor % 2 == 0:
            total_time += time_to_even_floors
        else:
            total_time += time_to_odd_floors

    # Convert the total time to minutes
    time_in_minutes = total_time / 60
    result = time_in_minutes
    return result

print(solution())