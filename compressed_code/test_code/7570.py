def solution():
    
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