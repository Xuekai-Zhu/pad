def solution():
    """Stacy went to a store to buy some pairs of shorts. Each pair normally cost $10, but there's a discount of 10% on the total cost for people who purchase 3 or more pairs at once. How much can she save by buying 3 pairs at once as opposed to purchasing them individually at different times?"""
    individual_cost = 10
    discount = 0.1
    # Cost of 3 individual pairs of shorts
    individual_total_cost = 3 * individual_cost
    # Cost of 3 pairs with discount
    discount_total_cost = individual_total_cost - (individual_total_cost * discount)
    # Savings by buying 3 at once
    savings = individual_total_cost - discount_total_cost
    result = savings
    return result

print(solution())