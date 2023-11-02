def solution():
    width = 200  # Width of the grassland in feet
    length = 900  # Length of the grassland in feet
    area = width * length  # Area of the grassland in square feet
    rabbits = 100  # Number of rabbits
    grass_eaten_per_rabbit_per_day = 10 / 9  # Conversion of square yards per day to square feet per day
    grass_eaten_per_day = rabbits * grass_eaten_per_rabbit_per_day  # Total grass eaten by all rabbits per day

    # Calculate number of days it would take for rabbits to clear all the grass
    days_to_clear_all_grass = area / grass_eaten_per_day
    result = days_to_clear_all_grass
    return result

print(solution())