def solution():
    """The school band is having a car wash to raise money. Their goal is to collect $150. So far they have earned $10 each from three families and $5 each from 15 families. How much more money do they have to earn to reach their goal?"""
    goal = 150
    money_collected = (10 * 3) + (5 * 15)
    remaining_money = goal - money_collected
    result = remaining_money
    return result

print(solution())