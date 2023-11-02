def solution():
    """Paul earns $12.50 for each hour that he works. He then has to pay 20% for taxes and fees. After working 40 hours, Paul receives his paycheck. If he spends 15% of his paycheck on gummy bears, how much, in dollars, does he have left?"""
    hourly_rate = 12.5
    total_hours_worked = 40
    gross_pay = hourly_rate * total_hours_worked
    taxes_and_fees = gross_pay * 0.2
    net_pay = gross_pay - taxes_and_fees
    gummy_bear_expense = net_pay * 0.15
    amount_left = net_pay - gummy_bear_expense
    result = amount_left
    return result

print(solution())