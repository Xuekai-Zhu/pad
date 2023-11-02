def solution():
    # Define Tim's initial number of cans
    initial_cans = 22

    # Subtract Jeff's cans
    remaining_cans = initial_cans - 6

    # Buy half the remaining amount
    bought_cans = 0.5 * remaining_cans

    # Add the bought cans to the remaining cans
    final_cans = remaining_cans + bought_cans
    result = final_cans
    return result

print(solution())