def solution():
    """Martin eats 1/2 cup of berries every day. The grocery store is selling a package of berries (1 cup per pack) for $2.00. How much will he spend on berries in a 30 day period?"""
    berries_per_day = 0.5
    cups_per_package = 1
    cost_per_package = 2.0
    days_per_period = 30
    total_cups = berries_per_day * days_per_period
    total_packages = total_cups / cups_per_package
    total_cost = total_packages * cost_per_package
    result = total_cost
    return result

print(solution())