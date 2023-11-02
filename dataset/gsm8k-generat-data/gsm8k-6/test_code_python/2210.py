def solution():
    # Calculate the number of packs needed to get 50 spoons
    spoons_per_pack = 30/3  # since there are equal number of knives, forks, and spoons
    packs_needed = 50/spoons_per_pack
    result = packs_needed
    return result

print(solution())