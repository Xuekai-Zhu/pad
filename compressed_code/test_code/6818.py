def solution():
    
    pies_per_batch = 5
    batches = 7
    total_pies_baked = pies_per_batch * batches
    pies_dropped = 8
    pies_left = total_pies_baked - pies_dropped
    result = pies_left
    return result

print(solution())