def solution():
    
    paul_daily_prayer = 20
    bruce_daily_prayer = paul_daily_prayer / 2
    sunday_prayer = paul_daily_prayer * 2
    paul_weekly_prayer = (paul_daily_prayer * 6) + sunday_prayer
    bruce_weekly_prayer = (bruce_daily_prayer * 6) + (sunday_prayer * 2)
    prayer_difference = paul_weekly_prayer - bruce_weekly_prayer
    result = prayer_difference
    return result

print(solution())