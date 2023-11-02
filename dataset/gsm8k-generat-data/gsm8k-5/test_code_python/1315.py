def solution():
    pies_per_batch = 5  # Marcus can fit 5 pies in his oven at once
    batches = 7  # Marcus bakes 7 batches of pies
    total_pies = pies_per_batch * batches  # Marcus bakes a total of 35 pies
    pies_dropped = 8  # Marcus drops 8 of the pies
    remaining_pies = total_pies - pies_dropped  # Calculate how many pies are left

    result = remaining_pies
    return result

print(solution())