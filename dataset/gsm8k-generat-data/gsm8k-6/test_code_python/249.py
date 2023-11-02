def solution():
    # Calculate the number of dandelion puffs Caleb has left after giving some to his family and his dog
    remaining_puffs = 40 - 3 - 3 - 5 - 2  # Caleb gave 3 puffs to his mom, 3 to his sister, 5 to his grandmother, and 2 to his dog

    # Calculate how many puffs each of his 3 friends would receive if they split the remaining puffs equally
    puffs_per_friend = remaining_puffs // 3  # using integer division to get a whole number without fractions

    result = puffs_per_friend
    return result

print(solution())