def solution():
    """Toby is counting goldfish in the local pond. He knows that only 25% of goldfish are at the surface and the rest are too deep below the surface to be able to see. If he counts 15 goldfish, how many are below the surface?"""
    # Define the proportion of goldfish at the surface
    surface_proportion = 0.25

    # Calculate the number of goldfish below the surface
    below_surface = (15 / (1 - surface_proportion)) - 15

    # return the result
    result = below_surface
    return result

print(solution())