def solution():
    """Tom has a job mowing lawns around his neighborhood. Each month he spends $17 on gas and mows 3 lawns, charging $12 per lawn mowed. Last month he also made extra money pulling weeds for $10. How much profit did Tom earn last month?"""
    gas_cost = 17
    lawn_cost = 12
    lawns_mowed = 3
    extra_money = 10
    total_income = (lawn_cost * lawns_mowed) + extra_money
    expenses = gas_cost
    profit = total_income - expenses
    result = profit
    return result

print(solution())