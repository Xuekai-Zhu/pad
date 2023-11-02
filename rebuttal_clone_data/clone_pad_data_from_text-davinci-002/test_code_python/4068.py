def solution():
    minutes_to_pick_cheap_cuffs = 6
    minutes_to_pick_expensive_cuffs = 8
    cuffs_on_hands = 3
    cuffs_on_ankles = 3
    total_cuffs = cuffs_on_hands + cuffs_on_ankles
    minutes_to_free_all = (minutes_to_pick_cheap_cuffs * cuffs_on_ankles) + (minutes_to_pick_expensive_cuffs * cuffs_on_hands)
    result = minutes_to_free_all
    
    return result

print(solution())