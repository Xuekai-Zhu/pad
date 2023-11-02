def solution():
    
    pies_per_batch = 5
    num_batches = 7
    total_pies = pies_per_batch * num_batches
    dropped_pies = 8
    remaining_pies = total_pies - dropped_pies
    result = remaining_pies
    return result

print(solution())