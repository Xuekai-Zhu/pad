def solution():
    """Bella eats 6 apples a day. If during the week she consumes a third of the apples Grace picks, how many apples will Grace have after 6 weeks?"""
    bella_apples_per_day = 6
    grace_apples_per_week = (bella_apples_per_day * 7) / 3
    weeks = 6
    total_grace_apples = grace_apples_per_week * weeks
    result = total_grace_apples
    return result

print(solution())