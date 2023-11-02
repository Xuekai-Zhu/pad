def solution():
    """Rita bought 5 short dresses, 3 pairs of pants and 4 jackets from a store that sells second-hand clothes. The dresses cost $20 each, the pants cost $12, the jackets cost $30 each, and she spent an additional $5 on transportation. If she had $400 initially, how much does she have now?"""
    dress_price = 20
    pants_price = 12
    jacket_price = 30
    transport_cost = 5
    total_cost = (5 * dress_price) + (3 * pants_price) + (4 * jacket_price) + transport_cost
    initial_fund = 400
    remaining_fund = initial_fund - total_cost
    result = remaining_fund
    return result

print(solution())