def solution():
    num_puffs = 40
    
    # Calculate the total number of puffs given away
    given_away = 3 + 3 + 5 + 2
    
    # Calculate the remaining number of puffs
    remaining_puffs = num_puffs - given_away
    
    # Calculate the number of puffs each friend received
    num_friends = 3
    puffs_per_friend = remaining_puffs // num_friends
    
    result = puffs_per_friend
    return result

print(solution())