def solution():
    
    gross_pay = 1120
    retirement_percent = 0.25
    taxes = 100
    retirement_amount = gross_pay * retirement_percent
    net_pay = gross_pay - retirement_amount - taxes
    result = net_pay
    return result

print(solution())