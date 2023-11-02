def solution():
    """Sheila, Purity, and Rose want to rent a house. Sheila has offered to pay five times Purity’s share of the rent. Rose can only afford thrice what Purity pays. If Rose’s share is $1,800, what is the total house rent?"""
    # Define the amount that Rose pays
    rose_share = 1800

    # Calculate the amount that Purity pays
    purity_share = rose_share / 3

    # Calculate the amount that Sheila pays
    sheila_share = purity_share * 5

    # Calculate the total rent
    total_rent = rose_share + purity_share + sheila_share

    # Return the result
    result = total_rent
    return result

print(solution())