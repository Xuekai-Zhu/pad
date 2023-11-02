def solution():
    total_floors = 20
    first_half_floors = total_floors / 2
    second_half_floors = total_floors - first_half_floors

    # Calculate time taken for first half of floors
    first_half_time = 15

    # Calculate time taken for next 5 floors
    second_half_time_1 = 5 * 5

    # Calculate time taken for final 5 floors
    second_half_time_2 = 16 * 5

    # Calculate total time taken in minutes
    total_time = first_half_time + second_half_time_1 + second_half_time_2

    # Convert to hours
    total_time_hours = total_time / 60
    result = total_time_hours
    return result

print(solution())