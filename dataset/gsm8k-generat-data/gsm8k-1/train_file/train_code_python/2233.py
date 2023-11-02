def solution():
    """Susie babysits every day for 3 hours a day at the rate of $10 per hour. She spent 3/10 of the money she earned from last week to buy a make-up set. She then spent 2/5 of her money on her skincare products. How much is left from her earnings last week, in dollars?"""
    hours_per_day = 3
    rate_per_hour = 10
    money_earned = hours_per_day * rate_per_hour * 7 # 7 days in a week
    makeup_spending = money_earned * (3/10)
    skincare_spending = money_earned * (2/5)
    remaining_money = money_earned - makeup_spending - skincare_spending
    result = remaining_money
    return result

print(solution())