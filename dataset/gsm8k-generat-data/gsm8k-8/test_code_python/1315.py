def solution():
    # Define the number of pies Marcus can fit in his oven and the number of batches he makes
    pies_per_batch = 5
    num_batches = 7

    # Calculate the total number of pies made and the number of dropped pies
    total_pies = pies_per_batch * num_batches
    dropped_pies = 8

    # Calculate the number of pies left
    pies_left = total_pies - dropped_pies
    result = pies_left
    return result

print(solution())