def solution():
    # Calculate the total number of berries picked
    total_pick = 30 + 20 + 10

    # Calculate the number of rotten berries
    rotten = total_pick / 3

    # Calculate the number of fresh berries
    fresh = total_pick - rotten

    # Calculate the number of berries to be kept
    kept = fresh / 2

    # Calculate the number of berries to be sold
    sold = fresh - kept

    result = sold
    return result

print(solution())