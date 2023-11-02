def solution():
    
    initial_puffs = 40
    puffs_given = 3 + 3 + 5 + 2
    puffs_remaining = initial_puffs - puffs_given
    puffs_per_friend = puffs_remaining / 3
    result = puffs_per_friend
    return result

print(solution())