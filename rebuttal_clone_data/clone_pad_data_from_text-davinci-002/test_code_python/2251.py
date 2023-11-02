def solution():
    gas_expense = 17
    lawns_mowed = 3
    price_per_lawn = 12
    other_income = 10
    total_income = lawns_mowed * price_per_lawn + other_income
    profit = total_income - gas_expense
    result = profit
    return result

print(solution())