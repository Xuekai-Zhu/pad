def solution():
    """Lorie earns $10 per hour. Karen earns twice what Lorie earns. How much does Karen earn in two days if she works 3 hours per day?"""
    lorie_pay = 10
    karen_pay = lorie_pay * 2
    hours_per_day = 3
    days = 2
    karen_total_earnings = karen_pay * hours_per_day * days
    result = karen_total_earnings
    return result

print(solution())