def solution():
    original_puffs = 40
    puffs_given_away = 3 + 3 + 5 + 2
    puffs_remaining = original_puffs - puffs_given_away
    puffs_per_friend = puffs_remaining / 3
    result = puffs_per_friend
    return result

print(solution())