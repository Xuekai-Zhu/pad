def solution():
    """A clothing store has an inventory of 34 ties, 40 belts, 63 black shirts, and 42 white shirts. The number of jeans in the store is two-thirds of the sum of black and white shirts, and the number of scarves is half the number of the sum of ties and belts. How many more jeans are there than scarves?"""
    ties = 34
    belts = 40
    black_shirts = 63
    white_shirts = 42
    jeans = (2/3 * (black_shirts + white_shirts))
    scarves = 1/2 * (ties + belts)
    difference = jeans - scarves
    result = difference
    return result

print(solution())