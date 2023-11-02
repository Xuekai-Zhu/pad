def solution():
    width = 200
    length = 900
    area = width * length

    # Convert area to square yards
    area_sq_yards = area / 9

    num_rabbits = 100
    grass_cleared_per_rabbit_per_day = 10

    # Calculate the total grass cleared per day by all rabbits
    total_grass_cleared_per_day = num_rabbits * grass_cleared_per_rabbit_per_day

    # Calculate the number of days it will take for rabbits to clear all grassland
    days_to_clear_grassland = area_sq_yards / total_grass_cleared_per_day
    result = days_to_clear_grassland
    return result

print(solution())