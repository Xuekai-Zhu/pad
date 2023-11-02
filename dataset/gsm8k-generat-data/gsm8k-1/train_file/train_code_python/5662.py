def solution():
    """The rate for mowing a lawn is $14 per hour. David mowed for 2 hours a day for a week. He then spent half of the money he made from mowing a lawn on a pair of shoes and gave half of the remaining money to his mom. How much money did he have left?"""
    rate_per_hour = 14
    hours_per_day = 2
    days_per_week = 7
    total_hours = hours_per_day * days_per_week
    total_earned = total_hours * rate_per_hour
    money_spent_on_shoes = total_earned / 2
    money_left = (total_earned - money_spent_on_shoes) / 2
    result = money_left
    return result

print(solution())