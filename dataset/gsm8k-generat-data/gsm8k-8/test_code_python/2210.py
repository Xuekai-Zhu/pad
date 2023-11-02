def solution():
    # Calculate the number of spoons in each pack (since there are an equal number of each utensil)
    spoons_per_pack = 30 / 3

    # Calculate the number of packs needed to get 50 spoons
    packs_needed = 50 / spoons_per_pack

    # Round up to the nearest whole number of packs
    packs_needed = math.ceil(packs_needed)

    result = packs_needed
    return result

print(solution())