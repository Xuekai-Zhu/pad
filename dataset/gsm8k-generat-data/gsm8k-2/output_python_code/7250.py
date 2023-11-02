def solution():
    """Melissa sells a coupe for $30,000 and an SUV for twice as much. If her commission is 2%, how much money did she make from these sales?"""
    coupe_price = 30000
    suv_price = 2 * coupe_price
    total_sales = coupe_price + suv_price
    commission_rate = 0.02
    commission = commission_rate * total_sales
    result = commission
    return result

print(solution())