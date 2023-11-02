def solution():
    # Calculate the total area of the walls
    wall_area = 5 * (2 * 3)  # 5 walls, each wall is 2m by 3m

    # Calculate the time needed to paint the entire room in minutes
    time_needed = wall_area * 10 * 60  # 1 square meter every 10 minutes and converting to minutes

    # Calculate the time available in minutes
    time_available = 10 * 60 * 60  # 10 hours converted to minutes

    # Calculate the time left in minutes
    time_left = time_available - time_needed

    # Convert the time left in minutes to hours
    hours_left = time_left / 60 / 60

    result = hours_left
    return result

print(solution())