def solution():
    """If you buy a dozen of doughnuts, it costs $8; but if you buy 2 dozens, it costs $14. How much will you save from buying 3 sets of 2 dozens than buying 6 sets of 1 dozen?"""
    # Define the cost of one dozen and two dozens of doughnuts
    ONE_DOZEN_PRICE = 8
    TWO_DOZENS_PRICE = 14

    # Calculate the cost of 3 sets of 2 dozens (6 dozens total)
    three_sets_cost = 3 * TWO_DOZENS_PRICE

    # Calculate the cost of 6 sets of 1 dozen (6 dozens total)
    six_sets_cost = 6 * ONE_DOZEN_PRICE

    # Calculate the savings from buying 3 sets of 2 dozens instead of 6 sets of 1 dozen
    savings = six_sets_cost - three_sets_cost

    # Display the savings
    result = savings
    return result

print(solution())