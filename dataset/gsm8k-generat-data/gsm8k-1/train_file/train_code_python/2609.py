def solution():
    """A farmer has 46 chickens. Each chicken gives him 6 eggs a week. If he sells a dozen eggs for $3, how much money would he make in 8 weeks?"""
    num_chickens = 46
    eggs_per_chicken_per_week = 6
    total_eggs_per_week = num_chickens * eggs_per_chicken_per_week
    dozen_eggs_per_week = total_eggs_per_week / 12
    price_per_dozen = 3
    total_money_per_week = dozen_eggs_per_week * price_per_dozen
    total_weeks = 8
    total_money = total_money_per_week * total_weeks
    result = total_money
    return result

print(solution())