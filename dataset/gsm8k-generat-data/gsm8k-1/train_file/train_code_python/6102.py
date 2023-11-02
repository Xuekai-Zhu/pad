def solution():
    """Tim has 22 cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys
    another half the amount of soda cans he had left. How many cans of soda does Tim have in the end?"""
    
    initial_cans = 22
    jeff_cans = 6
    remaining_cans = initial_cans - jeff_cans
    bought_cans = remaining_cans / 2
    total_cans = remaining_cans + bought_cans
    result = total_cans
    
    return result

print(solution())