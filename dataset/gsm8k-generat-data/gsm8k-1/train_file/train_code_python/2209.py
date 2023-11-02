def solution():
    """John decides to buy utensils. They come in 30 packs with an equal number of knives, forks, and spoons. How many packs does he need to buy if he wants 50 spoons?"""
    utensils_per_pack = 30
    spoons_per_pack = utensils_per_pack / 3  # Assuming that each pack has an equal number of knives, forks, and spoons
    spoons_needed = 50
    packs_needed = spoons_needed / spoons_per_pack

    result = packs_needed
    return result

print(solution())