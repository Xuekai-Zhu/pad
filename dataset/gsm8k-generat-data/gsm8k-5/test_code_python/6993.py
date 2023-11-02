def solution():
    walls = 5
    wall_width = 2
    wall_height = 3
    time_per_square_meter = 10  # Minutes per square meter
    time_available = 600  # Minutes (10 hours)

    # Calculate the total area of the walls
    total_area = walls * wall_width * wall_height

    # Calculate the total time it will take to paint the walls
    total_time = total_area * time_per_square_meter

    # Calculate the time Tom has to spare
    time_spare = (time_available - total_time) / 60  # Convert minutes to hours
    result = time_spare
    return result

print(solution())