def solution():
    
    total_cows = 140
    red_spots = total_cows * 0.4
    cows_without_red_spots = total_cows - red_spots
    blue_spots = cows_without_red_spots * 0.25
    cows_without_spots = total_cows - red_spots - blue_spots
    result = cows_without_spots
    return result

print(solution())