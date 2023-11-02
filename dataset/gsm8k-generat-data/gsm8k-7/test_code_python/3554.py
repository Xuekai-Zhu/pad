def solution():
    total_fish = 90
    swordfish_ratio = 5
    pufferfish_ratio = 1

    # Calculate the total ratio of swordfish to pufferfish
    total_ratio = swordfish_ratio + pufferfish_ratio

    # Calculate the fraction of the total that represents pufferfish
    pufferfish_fraction = pufferfish_ratio / total_ratio

    # Calculate the number of pufferfish
    num_pufferfish = pufferfish_fraction * total_fish
    result = num_pufferfish
    return result

print(solution())