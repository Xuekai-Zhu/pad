def solution():
    gross_pay = 1120
    retirement_percent = 0.25
    tax_deduction = 100

    # Calculate the amount going into Jim's retirement account
    retirement_savings = gross_pay * retirement_percent

    # Subtract retirement savings and tax deduction from gross pay to get net pay
    net_pay = gross_pay - retirement_savings - tax_deduction
    result = net_pay
    return result

print(solution())