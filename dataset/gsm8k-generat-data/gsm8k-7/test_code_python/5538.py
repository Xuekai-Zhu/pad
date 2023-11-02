def solution():
    cattle_count = 555
    cow_ratio = 10
    bull_ratio = 27

    # Calculate the total ratio
    total_ratio = cow_ratio + bull_ratio

    # Calculate the fraction of bulls in the total ratio
    bull_fraction = bull_ratio / total_ratio

    # Calculate the number of bulls on the farm
    num_bulls = bull_fraction * cattle_count
    result = num_bulls
    return result

print(solution())