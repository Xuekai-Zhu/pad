def solution():
    """Marcus can fit 5 pies in his oven at once. He bakes 7 batches of pies, then slips and drops 8 of them. How many pies are left?"""
    pies_per_batch = 5
    num_batches = 7
    total_pies = pies_per_batch * num_batches
    dropped_pies = 8
    remaining_pies = total_pies - dropped_pies
    result = remaining_pies
    return result

print(solution())