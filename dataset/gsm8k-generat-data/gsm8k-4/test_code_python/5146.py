def solution():
    """The bagels cost $2.25 each, or a dozen for $24. How much is saved, per bagel, in cents, by buying a dozen at a time?"""
    # Define the cost of a single bagel and the cost of a dozen bagels
    single_bagel_cost = 2.25
    dozen_bagel_cost = 24 / 12

    # Calculate the savings per bagel
    savings_per_bagel = round((single_bagel_cost - dozen_bagel_cost)*100)

    # Return the result
    result = savings_per_bagel
    return result

print(solution())