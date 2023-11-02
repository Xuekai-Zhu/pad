def solution():
    """If you buy a dozen of doughnuts, it costs $8; but if you buy 2 dozens, it costs $14. How much will you save from buying 3 sets of 2 dozens than buying 6 sets of 1 dozen?"""
    # Define the prices of 1 dozen and 2 dozens of doughnuts
    price_1dozen = 8
    price_2dozen = 14

    # Calculate the cost of buying 3 sets of 2 dozens
    cost_3sets_2dozen = 3 * price_2dozen

    # Calculate the cost of buying 6 sets of 1 dozen
    cost_6sets_1dozen = 6 * price_1dozen

    # Calculate the savings from buying 3 sets of 2 dozens instead of 6 sets of 1 dozen
    savings = cost_6sets_1dozen - cost_3sets_2dozen

    result = savings
    return result

print(solution())