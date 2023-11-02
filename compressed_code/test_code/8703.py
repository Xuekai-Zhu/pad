def solution():
    
    blue_picks = 12
    total_picks = blue_picks / (1/3)
    red_picks = total_picks / 2
    yellow_picks = total_picks - blue_picks - red_picks
    result = yellow_picks
    
    return result

print(solution())