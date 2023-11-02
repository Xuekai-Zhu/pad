def solution():
    # Define variables
    martha_cans = 90
    diego_cans = 0.5 * martha_cans + 10
    total_cans = martha_cans + diego_cans

    # Calculate how many more cans they need
    more_cans_needed = 150 - total_cans
    result = more_cans_needed
    return result

print(solution())