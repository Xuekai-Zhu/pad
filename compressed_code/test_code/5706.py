def solution():
    
    newspaper_minutes_per_week = 5 * 30
    novel_minutes_per_week = 5 * 60
    weekend_newspaper_minutes = 2 * (30 * 2)
    weekend_novel_minutes = 2 * (60 * 2)
    total_minutes_per_week = newspaper_minutes_per_week + novel_minutes_per_week + weekend_newspaper_minutes + weekend_novel_minutes
    result = total_minutes_per_week
    return result

print(solution())