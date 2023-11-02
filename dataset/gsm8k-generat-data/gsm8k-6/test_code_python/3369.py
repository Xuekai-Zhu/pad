def solution():
    # Calculate the total number of berries picked
    total_beries = 30 + 20 + 10

    # Calculate the number of rotten berries
    rotten_beries = total_beries / 3

    # Calculate the number of fresh berries
    fresh_beries = total_beries - rotten_beries

    # Calculate the number of berries to be kept
    kept_beries = fresh_beries / 2

    # Calculate the number of berries to be sold
    sold_beries = fresh_beries - kept_beries

    result = sold_beries
    return result

print(solution())