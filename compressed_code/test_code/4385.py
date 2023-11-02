def solution():
    
    pay = 500
    tax_percent = 10
    tax_amount = (tax_percent / 100) * pay
    take_home_pay = pay - tax_amount
    result = take_home_pay
    return result

print(solution())