def solution():
    # Set up the variables
    total_cans = 24
    start_cans = x

    # Jeff takes 6 cans
    remaining_cans = start_cans - 6

    # Tim buys half the amount he had left
    purchased_cans = remaining_cans / 2

    # Add the remaining and purchased cans to get total cans
    final_cans = remaining_cans + purchased_cans

    # Solve for the initial number of cans using the final number of cans
    start_cans = final_cans / 0.75

    result = start_cans
    return result

print(solution())