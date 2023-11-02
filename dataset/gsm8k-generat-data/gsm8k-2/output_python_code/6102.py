def solution():
    """Tim has 22 cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. How many cans of soda does Tim have in the end?"""
    initial_cans = 22
    cans_taken = 6
    remaining_cans = initial_cans - cans_taken
    additional_cans = remaining_cans / 2
    total_cans = remaining_cans + additional_cans
    result = total_cans
    return result

print(solution())