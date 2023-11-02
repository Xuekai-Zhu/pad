def solution():
    """Jim’s bi-weekly gross pay is $1120. He automatically has 25% of his paycheck go into his retirement account. They also take $100.00 out of each paycheck for taxes. After money is taken out for retirement and taxes, how much money will be on Jim’s paycheck?"""
    # Define Jim's bi-weekly gross pay
    bi_weekly_pay = 1120

    # Calculate the amount going into Jim's retirement account
    retirement = bi_weekly_pay * 0.25

    # Calculate the amount taken out for taxes
    taxes = 100

    # Calculate the total deductions
    total_deductions = retirement + taxes

    # Calculate Jim's net pay
    net_pay = bi_weekly_pay - total_deductions

    result = net_pay
    return result

print(solution())