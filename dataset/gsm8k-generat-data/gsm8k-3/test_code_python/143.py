def solution():
    """Toby is counting goldfish in the local pond. He knows that only 25% of goldfish are at the surface and the rest are too deep below the surface to be able to see. If he counts 15 goldfish, how many are below the surface?"""
    # Define the percentage of goldfish below the surface
    below_surface_percentage = 75

    # Calculate the total number of goldfish
    total_goldfish = 15 / 0.25

    # Calculate the number of goldfish below the surface
    below_surface_goldfish = total_goldfish - 15

    result = below_surface_goldfish
    return result

print(solution())