def solution():
    """Stacy went to a store to buy some pairs of shorts. Each pair normally cost $10, but there's a discount of 10% on the total cost for people who purchase 3 or more pairs at once. How much can she save by buying 3 pairs at once as opposed to purchasing them individually at different times?"""
    # Define the cost of one pair of shorts
    SHORTS_COST = 10

    # Define the number of pairs of shorts Stacy wants to buy
    shorts_count = 3

    # Calculate the total cost of buying the shorts individually
    individual_cost = SHORTS_COST * shorts_count

    # Calculate the discounted cost of buying the shorts together
    if shorts_count >= 3:
        discounted_cost = (SHORTS_COST * shorts_count) * 0.9
    else:
        discounted_cost = individual_cost

    # Calculate the amount saved by buying the shorts together
    saved_amount = individual_cost - discounted_cost

    # Return the saved amount
    result = saved_amount
    return result

print(solution())