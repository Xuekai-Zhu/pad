def solution():
    """Out of the 200 apples in an orchard, 40 percent were rotten. Also, 70 percent of the rotten apples smelled. How many rotten apples in the orchard did not smell?"""
    total_apples = 200
    rotten_percent = 40
    rotten_apples = (rotten_percent / 100) * total_apples
    smelling_apples = 0.7 * rotten_apples
    not_smelling_apples = rotten_apples - smelling_apples
    result = not_smelling_apples
    return result

print(solution())