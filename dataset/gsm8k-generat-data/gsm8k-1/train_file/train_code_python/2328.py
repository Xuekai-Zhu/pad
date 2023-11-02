def solution():
    """Archie received his medical receipt from his doctor, and he needs to take antibiotics three times a day. If antibiotic costs $3 each and he needs to take it for a week, how much money does he need to buy the antibiotics?"""
    antibiotic_cost = 3
    antibiotics_per_day = 3
    days_per_week = 7
    total_antibiotics = antibiotics_per_day * days_per_week
    total_cost = antibiotic_cost * total_antibiotics
    result = total_cost
    return result

print(solution())