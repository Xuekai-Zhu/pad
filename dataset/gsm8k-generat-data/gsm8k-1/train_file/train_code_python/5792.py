def solution():
    """The dog toys Samantha buys for her dog are "buy one get one half off" and all cost $12.00 each. She buys 4 toys. How much does she spend on dog toys?"""
    toy_cost = 12
    num_toys = 4
    full_price_toys = num_toys // 2
    half_price_toys = num_toys - full_price_toys
    total_cost = (full_price_toys * toy_cost) + (half_price_toys * (toy_cost/2))
    result = total_cost
    return result

print(solution())