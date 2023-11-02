def solution():
    """Sarah uses 1 ounce of shampoo, and one half as much conditioner as shampoo daily. In two weeks, what is the total volume of shampoo and conditioner, in ounces, that Sarah will use?"""
    shampoo_daily = 1
    conditioner_daily = shampoo_daily / 2
    total_daily = shampoo_daily + conditioner_daily
    total_biweekly = total_daily * 14
    result = total_biweekly
    return result

print(solution())