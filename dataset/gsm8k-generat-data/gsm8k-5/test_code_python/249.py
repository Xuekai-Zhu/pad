def solution():
    original_puffs = 40  # Caleb originally picked 40 dandelion puffs
    given_to_others = 3 + 3 + 5 + 2  # Caleb gave away a total of 13 dandelion puffs
    remaining_puffs = original_puffs - given_to_others  # Caleb has this many puffs left to divide among his friends
    friends = 3  # Caleb has 3 friends to divide the remaining puffs among

    # Calculate how many puffs each friend will receive
    puffs_per_friend = remaining_puffs // friends
    result = puffs_per_friend
    return result

print(solution())