def solution():
    rain_mon_am = 2
    rain_mon_pm = 1
    rain_tues = rain_mon_am * 2
    rain_thurs = 1
    rain_fri = rain_mon_am + rain_mon_pm + rain_tues + rain_thurs
    rain_week = rain_mon_am + rain_mon_pm + rain_tues + rain_thurs + rain_fri
    rain_avg = rain_week / 5
    result = rain_avg
    return result

print(solution())