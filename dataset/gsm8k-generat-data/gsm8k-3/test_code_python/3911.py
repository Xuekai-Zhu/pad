def solution():
    """Bill is doing weight training before trying out for the boxing team. He gets two 2-gallon jugs and fills them 70% full with sand. If sand has a density of 5 pounds/gallon, how many pounds do Bill's improvised weights weigh?"""
    # Define the volume of each jug and the percentage they are filled with sand
    VOLUME_PER_JUG = 2
    FILL_PERCENTAGE = 0.7

    # Calculate the volume of sand in each jug
    sand_volume = VOLUME_PER_JUG * FILL_PERCENTAGE

    # Calculate the weight of the sand in each jug
    sand_weight = sand_volume * 5

    # Calculate the total weight of both jugs filled with sand
    total_weight = sand_weight * 2

    # Display the total weight
    result = total_weight
    return result

print(solution())