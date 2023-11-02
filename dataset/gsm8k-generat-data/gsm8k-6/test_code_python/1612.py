def solution():
    # Calculate Paul's gross pay
    gross_pay = 12.50 * 40

    # Calculate the total amount of taxes and fees Paul has to pay
    taxes_and_fees = gross_pay * 0.20

    # Calculate Paul's net pay after taxes and fees
    net_pay = gross_pay - taxes_and_fees

    # Calculate the amount of money Paul spends on gummy bears
    gummy_bear_expenses = net_pay * 0.15

    # Calculate Paul's remaining money after expenses
    remaining_money = net_pay - gummy_bear_expenses
    result = remaining_money
    return result

print(solution())