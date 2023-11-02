def solution():
    """Lucas went to the store with $20 and needed to buy 3 avocados that cost $2 each. How much change does he bring home?"""
    initial_amount = 20
    num_avocados = 3
    avocado_cost = 2
    total_cost = num_avocados * avocado_cost
    change = initial_amount - total_cost
    result = change
    return result

print(solution())