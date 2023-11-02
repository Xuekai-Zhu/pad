def solution():
    total_pebbles = 40  # total number of pebbles collected by Shawn
    red_pebbles = 9  # number of pebbles painted red
    blue_pebbles = 13  # number of pebbles painted blue
    remaining_pebbles = total_pebbles - red_pebbles - blue_pebbles  # number of pebbles remaining to be painted
    each_group_pebbles = remaining_pebbles // 3  # number of pebbles in each group after dividing remaining pebbles equally
    yellow_pebbles = each_group_pebbles  # number of pebbles painted yellow
    blue_yellow_diff = blue_pebbles - yellow_pebbles  # difference between the number of blue and yellow pebbles
    result = blue_yellow_diff
    return result

print(solution())