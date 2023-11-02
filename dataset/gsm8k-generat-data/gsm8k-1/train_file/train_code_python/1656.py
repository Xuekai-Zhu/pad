def solution():
    """Sheila, Purity, and Rose want to rent a house. Sheila has offered to pay five times Purity’s share of the rent. Rose can only afford thrice what Purity pays. If Rose’s share is $1,800, what is the total house rent?"""
    rose_share = 1800
    purity_share = rose_share / 3
    sheila_share = 5 * purity_share
    total_rent = rose_share + purity_share + sheila_share
    result = total_rent
    return result

print(solution())