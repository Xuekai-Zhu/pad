def solution():
    # Find Purity's share of the rent
    purity_share = 1800 / 3

    # Find Sheila's share of the rent
    sheila_share = 5 * purity_share

    # Find the total rent
    total_rent = purity_share + sheila_share + 1800

    result = total_rent
    return result

print(solution())