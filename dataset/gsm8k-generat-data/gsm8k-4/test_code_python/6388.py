def solution():
    """Tim has some cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. If Tim has 24 cans of soda in the end, how many cans of soda did Tim have at first?"""
    # Define the initial number of soda cans
    initial_cans = None

    # Define the number of cans Jeff took
    jeff_cans = 6

    # Calculate the number of cans after Jeff took some
    remaining_cans = 24 + jeff_cans

    # Calculate the number of cans Tim had before buying more
    before_buying_cans = remaining_cans * 2

    # Calculate the initial number of cans Tim had
    initial_cans = before_buying_cans + jeff_cans

    result = initial_cans
    return result

print(solution())