def solution():
    
    total_cows = 140
    red_spot_cows = 0.4 * total_cows
    non_red_cows = total_cows - red_spot_cows
    blue_spot_cows = 0.25 * non_red_cows
    no_spot_cows = non_red_cows - blue_spot_cows
    result = no_spot_cows
    return result

print(solution())