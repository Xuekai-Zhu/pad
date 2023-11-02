def solution():
    """Stacy went to a store to buy some pairs of shorts. Each pair normally cost $10, but there's a discount of 10% on the total cost for people who purchase 3 or more pairs at once. How much can she save by buying 3 pairs at once as opposed to purchasing them individually at different times?"""
    price_per_pair = 10
    num_pairs = 3
    total_cost_individual = price_per_pair * num_pairs
    total_cost_discounted = total_cost_individual * 0.9
    savings = total_cost_individual - total_cost_discounted
    result = savings
    return result

print(solution())