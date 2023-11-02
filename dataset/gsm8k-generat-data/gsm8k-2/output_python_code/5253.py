def solution():
    """Shawn collected 40 plain pebbles. He painted 9 pebbles red and 13 pebbles blue. He then divided the remaining pebbles equally into 3 groups, and painted them purple, yellow, and green. What is the difference between the number of blue and yellow pebbles?"""
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