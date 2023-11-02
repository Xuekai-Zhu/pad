def solution():
    crabs_per_day = 40  # Johnny makes his signature crab dish 40 times a day
    crab_weight = 1.5  # Each dish uses 1.5 pounds of crab meat
    crab_price = 8  # Crab meat sells for $8 per pound
    days_open_per_week = 7 - 3  # Johnny is closed for 3 days per week

    # Calculate the total amount of crab used per week
    crab_per_week = crabs_per_day * days_open_per_week * crab_weight

    # Calculate the total cost of crab meat per week
    crab_cost_per_week = crab_per_week * crab_price
    result = crab_cost_per_week
    return result

print(solution())