def solution():
    speed_normal_space = 2  # Zargon Destroyer travels 2 billion miles per hour in normal space
    speed_black_hole = speed_normal_space * 3  # Zargon Destroyer travels three times faster through black holes

    time_normal_space = 7  # Zargon Destroyer travels for 7 hours in normal space
    time_black_hole = 2  # Zargon Destroyer travels for 2 hours through a black hole

    # Calculate the distance traveled in normal space
    distance_normal_space = speed_normal_space * time_normal_space

    # Calculate the distance traveled in the black hole
    distance_black_hole = speed_black_hole * time_black_hole

    # Calculate the total distance traveled
    total_distance = distance_normal_space + distance_black_hole

    # Convert the total distance to billions of miles
    billions_of_miles = total_distance / 1000000000
    result = billions_of_miles
    return result

print(solution())