def solution():
    hourly_pay = 15
    weekly_hours = 40
    weeks_per_year = 52
    tax_withholding = 0.2

    # Calculate Trisha's gross pay per week
    gross_pay = hourly_pay * weekly_hours

    # Calculate Trisha's weekly pay after tax withholding
    net_pay_weekly = gross_pay * (1 - tax_withholding)

    # Calculate Trisha's annual net pay
    net_pay_annual = net_pay_weekly * weeks_per_year

    result = net_pay_annual
    return result

print(solution())