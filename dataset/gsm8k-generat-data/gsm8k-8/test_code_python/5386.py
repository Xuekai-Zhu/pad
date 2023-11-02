def solution():
    trolls_by_path = 6
    trolls_under_bridge = 4 * trolls_by_path - 6
    trolls_in_plains = trolls_under_bridge / 2
    
    total_trolls = trolls_by_path + trolls_under_bridge + trolls_in_plains
    result = total_trolls
    return result

print(solution())