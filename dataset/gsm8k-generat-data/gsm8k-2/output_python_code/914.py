def solution():
    """A sixty bulb watt uses 60 watts of power each day. If Allyn has 40 such bulbs in his house and pays an electricity bill of twenty cents per power watt used, calculate Allyn's total monthly expenses on electricity in June."""
    watts_per_day = 60 * 40
    watts_per_month = watts_per_day * 30
    cost_per_watt = 0.20
    total_cost = watts_per_month * cost_per_watt
    result = total_cost
    return result

print(solution())