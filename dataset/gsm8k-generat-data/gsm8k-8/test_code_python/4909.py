def solution():
    total_cows = 140
    cows_with_redSpot = 0.4 * total_cows
    cows_without_redSpot = total_cows - cows_with_redSpot
    cows_with_blueSpot = 0.25 * cows_without_redSpot
    cows_with_noSpot = total_cows - cows_with_redSpot - cows_with_blueSpot
    result = cows_with_noSpot
    return result

print(solution())