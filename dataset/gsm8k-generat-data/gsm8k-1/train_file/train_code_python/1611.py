def solution():
    """Paul earns $12.50 for each hour that he works. He then has to pay 20% for taxes and fees. After working 40 hours, Paul receives his paycheck. If he spends 15% of his paycheck on gummy bears, how much, in dollars, does he have left?"""
    wage_per_hour = 12.50
    work_hours = 40
    gross_pay = wage_per_hour * work_hours
    taxes_and_fees_percent = 20
    net_pay = gross_pay - (gross_pay * (taxes_and_fees_percent / 100))
    gummy_bear_percent = 15
    money_spent_on_gummy_bears = net_pay * (gummy_bear_percent / 100)
    money_left = net_pay - money_spent_on_gummy_bears
    result = money_left
    return result

print(solution())