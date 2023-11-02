def solution():
    total_pebbles = 40
    red_pebbles = 9
    blue_pebbles = 13
    purple_pebbles = (total_pebbles - red_pebbles - blue_pebbles) // 3
    yellow_pebbles = purple_pebbles
    green_pebbles = purple_pebbles
    result = abs(blue_pebbles - yellow_pebbles)
    return result

print(solution())