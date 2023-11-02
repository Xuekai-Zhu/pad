def solution():
    """Stacy went to a store to buy some pairs of shorts. Each pair normally cost $10, but there's a discount of 10% on the total cost for people who purchase 3 or more pairs at once. How much can she save by buying 3 pairs at once as opposed to purchasing them individually at different times?"""
    # Define the original cost per pair
    ORIGINAL_PRICE = 10

    # Define the number of pairs Stacy wants to buy
    num_pairs = 3

    # Calculate the cost of buying them individually
    individual_cost = num_pairs * ORIGINAL_PRICE

    # Calculate the cost of buying them together with the discount
    discount_cost = (num_pairs * ORIGINAL_PRICE) * 0.9

    # Calculate the amount saved
    amount_saved = individual_cost - discount_cost

    # Display the amount saved
    result = amount_saved
    return result

print(solution())