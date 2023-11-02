def solution():
    """The news announced a $0.4 oil price rollback this Friday. Mr. Deane decided to only fill his gas tank with 10 liters of gas today and then another 25 liters on Friday. If the cost per liter of gas is $1.4 today, how much will Mr. Deane spend for his 35 liters of gas?"""
    liters_today = 10
    liters_friday = 25
    cost_per_liter = 1.4
    total_cost = (liters_today + liters_friday) * (cost_per_liter - 0.4)
    result = total_cost
    return result

print(solution())