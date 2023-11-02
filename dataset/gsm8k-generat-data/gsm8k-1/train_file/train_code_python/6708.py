def solution():
    """Rita bought 5 short dresses, 3 pairs of pants and 4 jackets from a store that sells second-hand clothes. The dresses cost $20 each, the pants cost $12, the jackets cost $30 each, and she spent an additional $5 on transportation. If she had $400 initially, how much does she have now?"""
    dress_cost = 20
    num_dresses = 5
    pant_cost = 12
    num_pants = 3
    jacket_cost = 30
    num_jackets = 4
    transport_cost = 5
    
    total_cost = (dress_cost * num_dresses) + (pant_cost * num_pants) + (jacket_cost * num_jackets) + transport_cost
    remaining_money = 400 - total_cost
    result = remaining_money
    return result

print(solution())