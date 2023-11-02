def solution():
    """Jim’s bi-weekly gross pay is $1120. He automatically has 25% of his paycheck go into his retirement account. They also take $100.00 out of each paycheck for taxes. After money is taken out for retirement and taxes, how much money will be on Jim’s paycheck?"""
    gross_pay = 1120
    retirement_percent = 0.25
    taxes = 100
    retirement_amount = gross_pay * retirement_percent
    net_pay = gross_pay - retirement_amount - taxes
    result = net_pay
    return result

print(solution())