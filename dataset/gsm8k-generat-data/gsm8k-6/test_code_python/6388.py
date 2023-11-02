def solution():
    # Calculate how many cans of soda Tim had before Jeff took 6
    initial_cans = 24 + 6  # Tim ends up with 24 cans in the end
    remaining_cans = initial_cans * 2  # Tim buys another half the amount he had left after Jeff took 6
    initial_cans = remaining_cans + 6  # Tim had 6 cans taken by Jeff
    result = initial_cans
    return result

print(solution())