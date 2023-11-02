def solution():
    """Mr. Caiden wants to do repairs to his house and requires 300 feet of metal roofing to do this. If each foot of roofing costs $8, and the supplier of the metal roofing brings in 250 feet of metal roofing for free, how much money is Mr. Caiden required to pay for the remaining metal roofing?"""
    total_roofing_needed = 300
    cost_per_foot = 8
    free_roofing = 250
    remaining_roofing_needed = total_roofing_needed - free_roofing
    total_cost = remaining_roofing_needed * cost_per_foot
    result = total_cost
    
    return result

print(solution())