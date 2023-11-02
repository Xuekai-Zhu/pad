def solution():
    
    gas_cost = 17
    lawn_count = 3
    lawn_price = 12
    weed_pulling_income = 10
    total_income = (lawn_count * lawn_price) + weed_pulling_income
    expenses = gas_cost
    profit = total_income - expenses
    result = profit
    return result

print(solution())