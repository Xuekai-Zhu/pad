def solution():
    
    total_fish = 66
    red_stripes = total_fish // 3
    remaining_fish = total_fish - red_stripes
    blue_stripes = remaining_fish * (5/11)
    total_red_and_blue_stripes = red_stripes + blue_stripes
    result = total_red_and_blue_stripes
    return result

print(solution())