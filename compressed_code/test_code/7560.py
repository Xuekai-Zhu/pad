def solution():
    
    morning_rice = 3
    afternoon_rice = 2
    evening_rice = 5
    cups_per_week = (morning_rice + afternoon_rice + evening_rice) * 7
    fat_per_cup = 10
    fat_per_week = cups_per_week * fat_per_cup
    result = fat_per_week
    return result

print(solution())