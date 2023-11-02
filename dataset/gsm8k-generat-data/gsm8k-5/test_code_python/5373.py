def solution():
    gross_pay = 1120  # Jim's bi-weekly gross pay is $1120
    retirement_percent = 0.25  # Jim's retirement account gets 25% of his paycheck
    tax_amount = 100  # $100 is taken out of each paycheck for taxes

    # Calculate the amount of money going into Jim's retirement account
    retirement_contribution = gross_pay * retirement_percent

    # Calculate the amount of money taken out for taxes
    taxes = tax_amount * 2  # Taxes are taken out of each bi-weekly paycheck

    # Calculate Jim's net pay after retirement contributions and taxes are taken out
    net_pay = gross_pay - retirement_contribution - taxes
    result = net_pay
    return result

print(solution())