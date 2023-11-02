def solution():
    hourly_rate = 12.5  # Paul earns $12.50 per hour
    hours_worked = 40  # Paul worked 40 hours
    gross_pay = hourly_rate * hours_worked  # Paul's gross pay before taxes and fees
    taxes_and_fees = 0.2 * gross_pay  # Paul pays 20% of his gross pay for taxes and fees
    net_pay = gross_pay - taxes_and_fees  # Paul's net pay after taxes and fees
    gummy_bear_expense = 0.15 * net_pay  # Paul spends 15% of his net pay on gummy bears
    remaining_pay = net_pay - gummy_bear_expense  # Paul's remaining pay after buying gummy bears
    result = remaining_pay
    return result

print(solution())