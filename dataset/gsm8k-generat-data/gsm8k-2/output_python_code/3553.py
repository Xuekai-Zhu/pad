def solution():
    """There are five times as many swordfish as pufferfish in an aquarium exhibit. If there are 90 fish total, how many pufferfish are there?"""
    total_fish = 90
    swordfish = 5 * pufferfish
    total_swordfish_and_pufferfish = swordfish + pufferfish
    pufferfish = total_fish / (5 + 1)
    result = pufferfish
    return result

print(solution())