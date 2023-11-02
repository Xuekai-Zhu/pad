def solution():
    muffins_ordered = 12
    price_ordered = 0.75
    selling_price = 1.5
    weekly_profit = (muffins_ordered * days_per_week * selling_price) - (muffins_ordered * days_per_week * price_ordered)
    result = weekly_profit
    return result

print(solution())