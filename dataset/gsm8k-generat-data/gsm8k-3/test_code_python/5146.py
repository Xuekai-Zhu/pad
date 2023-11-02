def solution():
    """The bagels cost $2.25 each, or a dozen for $24. How much is saved, per bagel, in cents, by buying a dozen at a time?"""
    # Define the cost of a single bagel and a dozen bagels
    SINGLE_PRICE = 2.25
    DOZEN_PRICE = 24

    # Calculate the cost of a bagel when bought individually
    single_cost = SINGLE_PRICE * 100 # convert to cents

    # Calculate the cost of a bagel when bought in a dozen
    dozen_cost = DOZEN_PRICE / 12 * 100 # convert to cents

    # Calculate the amount saved per bagel when bought in a dozen
    saved_per_bagel = single_cost - dozen_cost / 12

    # Display the amount saved per bagel in cents
    result = saved_per_bagel
    return result

print(solution())