def solution():
    # Determine the total area of the walls
    wall_area = 5 * (2 * 3)

    # Determine the total time it will take to paint the walls (in minutes)
    total_time = wall_area * 10

    # Convert total time to hours
    total_time_hours = total_time / 60

    # Determine the time John has to spare (in hours)
    time_left = 10 - total_time_hours

    result = time_left
    return result

print(solution())