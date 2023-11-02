def solution():
    """Vince can staple 30 reports every 15 minutes. If he was stapling reports from 8:00 AM until 11:00 PM, how many reports did he staple altogether?"""
    reports_per_15_minutes = 30
    minutes_per_hour = 60
    hours_worked = 15
    start_time = 8
    end_time = 23
    total_minutes_worked = (end_time - start_time) * 60
    total_reports_stapled = (total_minutes_worked // minutes_per_hour) * (reports_per_15_minutes // 2)
    result = total_reports_stapled
    return result

print(solution())