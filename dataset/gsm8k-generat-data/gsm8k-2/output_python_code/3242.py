def solution():
    """Bella eats 6 apples a day. If during the week she consumes a third of the apples Grace picks, how many apples will Grace have after 6 weeks?"""
    bella_apples_per_week = 6 * 7
    grace_apples_per_week = 3 * bella_apples_per_week
    total_grace_apples = grace_apples_per_week * 6
    result = total_grace_apples
    return result

print(solution())