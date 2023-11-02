def solution():
    """Clinton buys a burger meal for lunch for $6.00 and up sizes his fries and drinks for $1.00 more. If Clinton buys this same meal every day for 5 days, how much does he spend on lunch?"""
    meal_cost = 6
    upgrade_cost = 1
    days = 5
    total_cost = (meal_cost + upgrade_cost) * days
    result = total_cost
    return result

print(solution())