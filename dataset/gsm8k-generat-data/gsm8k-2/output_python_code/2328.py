def solution():
    """Archie received his medical receipt from his doctor, and he needs to take antibiotics three times a day. If antibiotic costs $3 each and he needs to take it for a week, how much money does he need to buy the antibiotics?"""
    antibiotic_cost = 3
    doses_per_day = 3
    total_doses = doses_per_day * 7
    total_cost = total_doses * antibiotic_cost
    result = total_cost
    return result

print(solution())