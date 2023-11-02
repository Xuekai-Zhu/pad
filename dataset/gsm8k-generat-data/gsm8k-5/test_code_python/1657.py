def solution():
    rose_share = 1800  # Rose can only afford $1,800 for her share of the rent
    purity_share = rose_share / 3  # Rose pays 3 times what Purity pays
    sheila_share = purity_share * 5  # Sheila pays 5 times what Purity pays
    total_rent = rose_share + purity_share + sheila_share  # The total rent is the sum of all three shares
    result = total_rent
    return result

print(solution())