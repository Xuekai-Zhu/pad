def solution():
    jug_size = 2  # gallons
    fill_percentage = 0.7
    sand_density = 5  # pounds/gallon

    # Calculate the total volume of sand in the jugs
    total_sand_volume = jug_size * fill_percentage * 2

    # Calculate the total weight of the sand in the jugs
    total_sand_weight = total_sand_volume * sand_density
    result = total_sand_weight
    return result

print(solution())