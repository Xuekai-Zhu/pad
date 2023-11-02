def solution():
    pies_per_batch = 5
    num_batches = 7
    dropped_pies = 8

    # Calculate the total number of pies baked
    total_pies = pies_per_batch * num_batches

    # Subtract the number of dropped pies
    pies_left = total_pies - dropped_pies
    result = pies_left
    return result

print(solution())