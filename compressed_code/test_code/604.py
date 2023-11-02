def solution():
    
    weekly_income = 500
    tax = 0.1 * weekly_income
    water_bill = 55
    tithe = 0.1 * weekly_income
    total_expenses = tax + water_bill + tithe
    remaining_money = weekly_income - total_expenses
    result = remaining_money
    return result

print(solution())