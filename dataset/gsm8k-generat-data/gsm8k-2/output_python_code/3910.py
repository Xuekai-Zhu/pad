def solution():
    """Bill is doing weight training before trying out for the boxing team. He gets two 2-gallon jugs and fills them 70% full with sand. If sand has a density of 5 pounds/gallon, how many pounds do Bill's improvised weights weigh?"""
    jug_size = 2  # gallons
    fill_percentage = 0.7
    sand_density = 5  # pounds/gallon

    # calculate the volume of sand in each jug
    sand_volume = jug_size * fill_percentage
    # calculate the weight of sand in each jug
    sand_weight = sand_volume * sand_density
    # calculate the total weight of both jugs
    total_weight = 2 * sand_weight

    result = total_weight
    return result

print(solution())