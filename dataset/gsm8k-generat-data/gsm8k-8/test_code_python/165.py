def solution():
    # Calculate the total distance traveled by the bus
    total_distance = 2 * (55 + 10)

    # Calculate the total time taken to travel the distance and stay at the destination
    total_time = (total_distance / 2) + (2 * 60)

    # Convert the total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())