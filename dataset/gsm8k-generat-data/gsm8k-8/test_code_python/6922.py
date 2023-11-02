def solution():
    # Convert the dimensions of the land to yards
    length_yards = 900/3
    width_yards = 200/3

    # Calculate the total area in square yards
    total_area = length_yards * width_yards

    # Convert the number of rabbits to the amount of grass they can clear in one day
    grass_cleared_per_day = 100 * 10 * 1.0/9

    # Calculate the number of days it would take for the rabbits to clear all the grass
    days_to_clear_grass = total_area / grass_cleared_per_day
    result = days_to_clear_grass
    return result

print(solution())