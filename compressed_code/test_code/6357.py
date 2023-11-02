def solution():
    
    initial_yards_per_day = 8
    percentage_increase = 50
    yards_per_day_with_lawnmower = initial_yards_per_day * (1 + percentage_increase/100)
    total_yards_per_week = yards_per_day_with_lawnmower * 7
    result = total_yards_per_week
    return result

print(solution())