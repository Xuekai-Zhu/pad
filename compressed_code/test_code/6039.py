def solution():
    
    income = 60000
    tax_percent = 18
    tax_amount = income * (tax_percent / 100)
    take_home_pay = income - tax_amount
    result = take_home_pay
    return result

print(solution())