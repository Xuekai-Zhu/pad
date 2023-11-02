def solution():
    
    basil_per_cup = 4
    basil_harvest_per_week = 16
    weeks = 8
    total_basil_harvested = basil_harvest_per_week * weeks
    cups_of_pesto = total_basil_harvested // basil_per_cup
    result = cups_of_pesto
    return result

print(solution())