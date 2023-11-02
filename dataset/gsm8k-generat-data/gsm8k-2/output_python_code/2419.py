def solution():
    """While on vacation in Hawaii, Steve and Georgia decided to ship pineapples to their home. Each pineapple costs $1.25 and they buy a dozen. It will cost $21.00 to ship all of them to their home. How much will each pineapple end up costing them?"""
    pineapple_cost = 1.25
    pineapples_per_dozen = 12
    total_pineapples = 12
    shipping_cost = 21
    total_cost = (pineapple_cost * total_pineapples) + shipping_cost
    cost_per_pineapple = total_cost / total_pineapples
    result = cost_per_pineapple
    return result

print(solution())