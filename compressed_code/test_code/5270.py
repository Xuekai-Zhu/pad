def solution():
    
    price_per_bar = 1.5
    sections_per_bar = 3
    smores_per_section = 1
    scouts = 15
    smores_per_scout = 2
    total_smores_needed = scouts * smores_per_scout
    sections_needed = total_smores_needed / smores_per_section
    bars_needed = sections_needed / sections_per_bar
    cost = bars_needed * price_per_bar
    result = cost
    return result

print(solution())