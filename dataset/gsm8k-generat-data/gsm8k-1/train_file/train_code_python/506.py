def solution():
    """James buys steaks for buy one get one free. The price is $15 per pound and he buys 20 pounds. How much did he pay for the steaks?"""
    price_per_pound = 15
    pounds_bought = 20
    pounds_paid_for = pounds_bought / 2
    total_cost = pounds_paid_for * price_per_pound
    result = total_cost
    return result

print(solution())