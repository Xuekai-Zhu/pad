def solution():
    total_cows = 140
    cows_with_red_spot = total_cows * 0.4
    cows_without_red_spot = total_cows - cows_with_red_spot
    cows_with_blue_spot = cows_without_red_spot * 0.25
    cows_without_spot = total_cows - (cows_with_red_spot + cows_with_blue_spot)
    result = cows_without_spot
    return result

print(solution())