def solution():
    total_cows = 140
    cows_with_red_spot = 0.4 * total_cows
    cows_without_red_spot = total_cows - cows_with_red_spot
    cows_with_blue_spot = 0.25 * cows_without_red_spot
    cows_with_no_spot = cows_without_red_spot - cows_with_blue_spot
    result = cows_with_no_spot
    return result

print(solution())