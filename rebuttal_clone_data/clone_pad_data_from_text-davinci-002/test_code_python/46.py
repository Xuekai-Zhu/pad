def solution():
    """Carolyn practices the piano for 20 minutes a day and the violin for three times as long. If she practice six days a week, how many minutes does she spend practicing in a month with four weeks?"""
    minutes_per_day_piano = 20
    minutes_per_day_violin = minutes_per_day_piano * 3
    days_per_week = 6
    weeks_per_month = 4
    minutes_per_month_piano = minutes_per_day_piano * days_per_week * weeks_per_month
    minutes_per_month_violin = minutes_per_day_violin * days_per_week * weeks_per_month
    total_minutes = minutes_per_month_piano + minutes_per_month_violin
    result = total_minutes
    return result

print(solution())