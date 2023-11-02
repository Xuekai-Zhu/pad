def solution():
    batches_per_day = 3
    baguettes_per_batch = 48

    # Calculate the total number of baguettes made in one day
    total_baguettes = batches_per_day * baguettes_per_batch

    # Calculate the total number of baguettes sold in one day
    total_sold = 37 + 52 + 49

    # Calculate the number of baguettes remaining
    num_remaining = total_baguettes - total_sold
    result = num_remaining
    return result

print(solution())