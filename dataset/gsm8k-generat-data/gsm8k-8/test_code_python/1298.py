def solution():
    # Calculate the total time the plane hovered in each time zone
    mountain_time = 3 + 2
    central_time = 4 + 2
    eastern_time = 2 + 2

    # Calculate the total time the plane hovered over the two days
    total_time = mountain_time + central_time + eastern_time

    result = total_time
    return result

print(solution())