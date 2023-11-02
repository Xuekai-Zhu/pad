def solution():
    """John decides to replace all his hats. He has enough hats to wear a different one every day for 2 weeks. If each hat costs $50 how much do his hats cost?"""
    hats_per_day = 1
    days_in_two_weeks = 14
    total_hats = hats_per_day * days_in_two_weeks
    cost_per_hat = 50
    total_cost = total_hats * cost_per_hat
    result = total_cost
    return result

print(solution())