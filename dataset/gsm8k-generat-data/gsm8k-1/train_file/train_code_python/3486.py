def solution():
    """Johnny makes his signature crab dish 40 times a day. It uses 1.5 pounds of crab meat. Crab meat sells for $8 per pound. How much does he spend in a week if he is closed 3 days a week?"""
    dishes_per_day = 40
    crab_per_dish = 1.5
    crab_cost_per_pound = 8
    days_per_week = 7 - 3 #Johnny is closed 3 days per week
    total_crab_used = dishes_per_day * crab_per_dish * days_per_week
    total_cost = total_crab_used * crab_cost_per_pound
    result = total_cost
    return result

print(solution())