def solution():
    """Tim had a birthday party with a clown that cost $100 an hour for 4 hours. He also rented a bounce house for half the time that cost 3 times as much an hour. Everything else for the party cost $1000. How much did his birthday cost?"""
    clown_cost = 100 * 4
    bounce_house_cost = (3 * 100) * 2
    other_costs = 1000
    total_cost = clown_cost + bounce_house_cost + other_costs
    result = total_cost
    return result

print(solution())