def solution():
    """The rate for mowing a lawn is $14 per hour. David mowed for 2 hours a day for a week. He then spent half of the money he made from mowing a lawn on a pair of shoes and gave half of the remaining money to his mom. How much money did he have left?"""
    rate = 14
    hours_per_day = 2
    days_per_week = 7
    total_hours = hours_per_day * days_per_week
    total_earnings = rate * total_hours
    shoes_cost = total_earnings / 2
    remaining_money = (total_earnings - shoes_cost) / 2
    result = remaining_money
    return result

print(solution())