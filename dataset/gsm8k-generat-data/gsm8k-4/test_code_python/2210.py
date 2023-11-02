def solution():
    """John decides to buy utensils. They come in 30 packs with an equal number of knives, forks, and spoons. How many packs does he need to buy if he wants 50 spoons?"""
    # Calculate the number of spoons in one pack
    spoons_per_pack = 30 / 3

    # Calculate the number of packs needed to get 50 spoons
    packs_needed = 50 / spoons_per_pack

    # Round up to the nearest whole number of packs
    packs_needed = math.ceil(packs_needed)

    result = packs_needed
    return result

print(solution())