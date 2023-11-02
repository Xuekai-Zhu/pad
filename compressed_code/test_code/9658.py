def solution():
    
    rows_planted = 400
    plants_per_row = 300
    total_plants = rows_planted * plants_per_row
    hours_worked = 20
    plants_per_hour = total_plants / hours_worked
    result = plants_per_hour
    return result

print(solution())