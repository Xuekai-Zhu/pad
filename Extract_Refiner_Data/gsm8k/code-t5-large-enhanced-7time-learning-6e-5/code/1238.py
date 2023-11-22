def solution():
    
    total_hats = 100
    red_hats = total_hats / 2
    remaining_hats = total_hats - red_hats
    blue_hats = (3/5) * remaining_hats
    white_hats = remaining_hats - blue_hats
    result = white_hats
    return result

print(solution())