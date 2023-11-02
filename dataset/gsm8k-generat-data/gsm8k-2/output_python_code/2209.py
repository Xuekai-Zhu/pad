def solution():
    """John decides to buy utensils. They come in 30 packs with an equal number of knives, forks, and spoons. How many packs does he need to buy if he wants 50 spoons?"""
    spoons_per_pack = 30 / 3  # Each pack contains an equal number of knives, forks, and spoons
    num_packs = 50 / spoons_per_pack
    # Round up to the nearest whole number of packs
    if num_packs % 1 != 0:
        num_packs = num_packs // 1 + 1
    result = num_packs
    return result

print(solution())