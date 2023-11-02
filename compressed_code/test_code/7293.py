def solution():
    
    yards_at_50 = 20
    yards_at_80 = yards_at_50 * 2
    temp_saturday = 50
    temp_sunday = 80
    throws_saturday = 20
    throws_sunday = 30
    total_yards_saturday = yards_at_50 * throws_saturday
    total_yards_sunday = yards_at_80 * throws_sunday
    total_yards = total_yards_saturday + total_yards_sunday
    result = total_yards
    return result

print(solution())