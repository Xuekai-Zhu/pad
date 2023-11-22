def solution():
    
    total_plants = 100
    indoor_plants = total_plants / 4
    remaining_plants = total_plants - indoor_plants
    outdoor_plants = (2/3) * remaining_plants
    flowering_plants = remaining_plants - outdoor_plants
    flowering_percentage = (flowering_plants / total_plants) * 100
    result = flowering_percentage
    return result

print(solution())