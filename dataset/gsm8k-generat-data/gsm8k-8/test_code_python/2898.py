def solution():
    # Define the number of floors and time to travel the first half
    total_floors = 20
    first_half_floors = total_floors / 2
    first_half_time = 15

    # Define the time to travel the next 5 floors
    next_5_floors_time = 5 * 5

    # Define the time to travel the final 5 floors
    final_5_floors_time = 16 * 5

    # Calculate the total time
    total_time = first_half_time + next_5_floors_time + final_5_floors_time

    # Convert the total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())