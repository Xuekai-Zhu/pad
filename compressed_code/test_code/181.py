def solution():
    
    total_puffs = 40
    puffs_given_away = 3 + 3 + 5 + 2
    remaining_puffs = total_puffs - puffs_given_away
    puffs_per_friend = remaining_puffs // 3
    result = puffs_per_friend
    return result

print(solution())