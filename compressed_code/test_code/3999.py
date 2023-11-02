def solution():
    
    normal_daily_production = 40 * 50
    normal_weekly_production = normal_daily_production * 7
    reduced_daily_production = normal_daily_production - 500
    reduced_weekly_production = reduced_daily_production * 7
    total_production = normal_weekly_production + reduced_weekly_production
    result = total_production
    return result

print(solution())