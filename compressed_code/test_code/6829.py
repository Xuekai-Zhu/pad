def solution():
    
    yards_monday = 20
    yards_tuesday = 2 * yards_monday
    yards_wednesday = yards_tuesday / 4
    total_yards = yards_monday + yards_tuesday + yards_wednesday
    total_cost = 2 * total_yards
    result = total_cost
    return result

print(solution())