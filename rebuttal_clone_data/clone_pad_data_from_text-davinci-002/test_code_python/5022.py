def solution():
    yards = 40
    time = 10
    
    yards_per_second = yards / time
    percent_increase = 40
    
    new_yards_per_second = yards_per_second + (yards_per_second * (percent_increase/100))
    
    new_yards = new_yards_per_second * time
    
    result = new_yards
    
    return result

print(solution())