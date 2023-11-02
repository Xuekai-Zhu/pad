def solution():
    # Calculate Trisha's gross pay per week
    gross_pay_per_week = 15 * 40  # hourly pay of $15 for 40 hours per week

    # Calculate the amount withheld for taxes, unemployment insurance, and social security
    withholding_percent = 20/100 # 20 percent of pay withheld
    withholding_amount = gross_pay_per_week * withholding_percent

    # Calculate Trisha's net pay per week
    net_pay_per_week = gross_pay_per_week - withholding_amount

    # Calculate Trisha's annual net pay
    annual_net_pay = net_pay_per_week * 52

    result = annual_net_pay
    return result

print(solution())