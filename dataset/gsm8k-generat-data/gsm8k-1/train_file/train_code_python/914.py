def solution():
    """A sixty bulb watt uses 60 watts of power each day. If Allyn has 40 such bulbs in his house and pays an electricity bill of twenty cents per power watt used, calculate Allyn's total monthly expenses on electricity in June."""
    watts_per_bulb = 60
    number_of_bulbs = 40
    daily_watt_usage = watts_per_bulb * number_of_bulbs
    monthly_watt_usage = daily_watt_usage * 30
    price_per_watt = 0.2
    monthly_expenses = monthly_watt_usage * price_per_watt
    result = monthly_expenses
    return result

print(solution())