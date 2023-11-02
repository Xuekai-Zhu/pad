def solution():
    """Out of the 200 apples in an orchard, 40 percent were rotten. Also, 70 percent of the rotten apples smelled. How many rotten apples in the orchard did not smell?"""
    total_apples = 200
    rotten_percent = 0.4
    rotten_apples = total_apples * rotten_percent
    smelled_percent = 0.7
    smelled_apples = rotten_apples * smelled_percent
    not_smelled_apples = rotten_apples - smelled_apples
    result = not_smelled_apples
    return result

print(solution())