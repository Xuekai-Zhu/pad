def solution():
    
    weekly_income = 500
    tax_rate = 10
    water_bill = 55
    tithe = 10
    
    taxes = weekly_income * (tax_rate / 100)
    tithes = weekly_income * (tithe / 100)
    total_deductions = taxes + tithes + water_bill
    money_left = weekly_income - total_deductions
    
    result = money_left
    return result

print(solution())