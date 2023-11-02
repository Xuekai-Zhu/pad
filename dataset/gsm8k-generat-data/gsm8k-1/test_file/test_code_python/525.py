def solution():
    """Tom bought a CD for $4, and a headphone set. In total, he paid $48. How many more CDs would Tom have been able to buy if he had decided not to buy the headphone set?"""
    total_cost = 48
    cd_cost = 4
    num_cds = (total_cost - cd_cost) // cd_cost
    result = num_cds
    return result

print(solution())