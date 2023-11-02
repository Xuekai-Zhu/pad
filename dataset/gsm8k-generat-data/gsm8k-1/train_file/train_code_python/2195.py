def solution():
    """John buys a pair of earbuds that cost $200. If tax was 15%, how much did he pay after tax?"""
    initial_price = 200
    tax_rate = 0.15
    tax_amount = initial_price * tax_rate
    total_price = initial_price + tax_amount
    result = total_price
    return result

print(solution())