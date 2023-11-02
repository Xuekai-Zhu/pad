def solution():
    """Jim’s bi-weekly gross pay is $1120.  He automatically has 25% of his paycheck go into his retirement account.  They also take $100.00 out of each paycheck for taxes.  After money is taken out for retirement and taxes, how much money will be on Jim’s paycheck?"""
    # Define Jim's bi-weekly gross pay
    gross_pay = 1120

    # Calculate the amount going into Jim's retirement account
    retirement_amount = gross_pay * 0.25

    # Calculate the amount of taxes withheld
    taxes_withheld = 100

    # Calculate Jim's net pay
    net_pay = gross_pay - retirement_amount - taxes_withheld

    # Display Jim's net pay
    result = net_pay
    return result

print(solution())