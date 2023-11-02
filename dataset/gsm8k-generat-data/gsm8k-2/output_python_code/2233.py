def solution():
    """Susie babysits every day for 3 hours a day at the rate of $10 per hour. She spent 3/10 of the money she earned from last week to buy a make-up set. She then spent 2/5 of her money on her skincare products. How much is left from her earnings last week, in dollars?"""
    hours_per_day = 3
    hourly_rate = 10
    total_hours_per_week = hours_per_day * 7
    total_earnings = total_hours_per_week * hourly_rate
    make_up_spending = 0.3 * total_earnings
    skincare_spending = 0.4 * total_earnings
    remaining_money = total_earnings - make_up_spending - skincare_spending
    result = remaining_money
    return result

print(solution())