def solution():
    """John buys a pair of earbuds that cost $200. If tax was 15%, how much did he pay after tax?"""
    cost = 200
    tax_rate = 0.15
    tax_amount = cost * tax_rate
    total_cost = cost + tax_amount
    result = total_cost
    return result

print(solution())