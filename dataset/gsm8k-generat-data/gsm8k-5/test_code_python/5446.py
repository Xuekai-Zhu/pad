def solution():
    num_floors = 10  # The building has 10 floors
    even_time = 15  # It takes 15 seconds to go up to an even-numbered floor
    odd_time = 9  # It takes 9 seconds to go up to an odd-numbered floor
    total_time = 0  # Initialize total time to go up the stairs

    for floor in range(1, num_floors+1):
        if floor % 2 == 0:
            total_time += even_time
        else:
            total_time += odd_time

    # Convert total time to minutes
    total_time_minutes = total_time / 60
    result = total_time_minutes
    return result

print(solution())