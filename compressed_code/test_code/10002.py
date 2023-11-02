def solution():
    
    gross_pay = 1120
    retirement_percent = 25
    tax_deduction = 100
    retirement_deduction = gross_pay * (retirement_percent / 100)
    net_pay = gross_pay - retirement_deduction - tax_deduction
    result = net_pay
    return result

print(solution())