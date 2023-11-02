def solution():
    """Toby is counting goldfish in the local pond. He knows that only 25% of goldfish are at the surface and the rest are too deep below the surface to be able to see. If he counts 15 goldfish, how many are below the surface?"""
    total_goldfish = 15
    surface_goldfish_percent = 25
    below_surface_goldfish_percent = 100 - surface_goldfish_percent
    below_surface_goldfish = (below_surface_goldfish_percent / 100) * total_goldfish
    result = below_surface_goldfish
    return result

print(solution())