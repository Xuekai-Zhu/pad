def solution():
    
    total_pebbles = 40
    red_pebbles = 9
    blue_pebbles = 13
    remaining_pebbles = total_pebbles - red_pebbles - blue_pebbles
    purple_pebbles = remaining_pebbles // 3
    yellow_pebbles = purple_pebbles
    green_pebbles = purple_pebbles
    blue_yellow_diff = blue_pebbles - yellow_pebbles
    result = blue_yellow_diff
    return result

print(solution())