def solution():
    """Mr. Caiden wants to do repairs to his house and requires 300 feet of metal roofing to do this. If each foot of roofing costs $8, and the supplier of the metal roofing brings in 250 feet of metal roofing for free, how much money is Mr. Caiden required to pay for the remaining metal roofing?"""
    needed_feet = 300
    cost_per_foot = 8
    free_feet = 250
    remaining_feet = needed_feet - free_feet
    total_cost = remaining_feet * cost_per_foot
    result = total_cost
    return result

print(solution())