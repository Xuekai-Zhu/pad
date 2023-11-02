def solution():
    """Bill is doing weight training before trying out for the boxing team. He gets two 2-gallon jugs and fills them 70% full with sand. If sand has a density of 5 pounds/gallon, how many pounds do Bill's improvised weights weigh?"""
    # Define the volume of each jug and the density of sand
    jug_volume = 2 # in gallons
    sand_density = 5 # in pounds/gallon

    # Calculate the volume of sand in each jug (70% full)
    sand_volume = jug_volume * 0.7

    # Calculate the weight of sand in each jug
    sand_weight = sand_volume * sand_density

    # Calculate the total weight of both jugs
    total_weight = sand_weight * 2

    result = total_weight
    return result

print(solution())