def solution():
    pies_per_batch = 5
    batches_baked = 7
    pies_dropped = 8
    pies_left = (pies_per_batch * batches_baked) - pies_dropped
    result = pies_left
    return result

print(solution())