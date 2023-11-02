def solution():
    """Tim has 22 cans of soda. Jeff comes by, and takes 6 cans of soda from Tim. Tim then goes and buys another half the amount of soda cans he had left. How many cans of soda does Tim have in the end?"""
    # Define the initial number of soda cans
    soda_cans = 22

    # Subtract the number of cans Jeff took
    soda_cans -= 6

    # Calculate the number of cans left for Tim to buy
    remaining_cans = soda_cans

    # Buy half of the remaining cans
    bought_cans = remaining_cans / 2

    # Add the bought cans to the original number of cans left
    soda_cans += bought_cans

    # Round the result to the nearest integer
    result = round(soda_cans)
    return result

print(solution())