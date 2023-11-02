def solution():
    """The school band is having a car wash to raise money. Their goal is to collect $150. So far they have earned $10 each from three families and $5 each from 15 families. How much more money do they have to earn to reach their goal?"""
    goal = 150
    money_from_first_group = 10 * 3
    money_from_second_group = 5 * 15
    total_money_so_far = money_from_first_group + money_from_second_group
    remaining_money = goal - total_money_so_far
    result = remaining_money
    return result

print(solution())