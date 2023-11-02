def solution():
    
    piano_minutes_per_week = 20 * 6
    violin_minutes_per_week = 3 * piano_minutes_per_week
    total_minutes_per_week = piano_minutes_per_week + violin_minutes_per_week
    total_minutes_per_month = total_minutes_per_week * 4
    result = total_minutes_per_month
    return result

print(solution())