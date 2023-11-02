def solution():
    """Each week Jaime saves $50. Every two weeks she spends $46 of her savings on a nice lunch with her mum. How long will it take her to save $135?"""
    savings_per_week = 50
    spending_per_two_weeks = 46
    target_savings = 135
    weeks_to_save = (target_savings + spending_per_two_weeks) / savings_per_week
    result = weeks_to_save
    return result

print(solution())