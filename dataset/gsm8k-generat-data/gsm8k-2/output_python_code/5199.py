def solution():
    """Bryan bought 5 t-shirts and 4 pairs of pants for $1500. If a t-shirt costs $100, how much does each pair of pants cost?"""
    total_cost = 1500
    num_shirts = 5
    shirt_cost = 100
    shirt_total_cost = num_shirts * shirt_cost
    pant_total_cost = total_cost - shirt_total_cost
    num_pants = 4
    pant_cost = pant_total_cost / num_pants
    result = pant_cost
    return result

print(solution())