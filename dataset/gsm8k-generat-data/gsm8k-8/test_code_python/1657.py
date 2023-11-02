def solution():
    # Define Rose's share
    rose_share = 1800

    # Calculate Purity's share
    purity_share = rose_share / 3

    # Calculate Sheila's share
    sheila_share = 5 * purity_share

    # Calculate the total rent
    total_rent = rose_share + purity_share + sheila_share
    result = total_rent
    return result

print(solution())