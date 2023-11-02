def solution():
    num_trolls_by_path = 6
    num_trolls_under_bridge = 4*num_trolls_by_path - 6
    num_trolls_in_plains = num_trolls_under_bridge / 2

    total_trolls = num_trolls_by_path + num_trolls_under_bridge + num_trolls_in_plains
    result = total_trolls
    return result

print(solution())