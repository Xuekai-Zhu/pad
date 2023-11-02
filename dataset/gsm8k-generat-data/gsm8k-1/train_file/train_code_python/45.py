def solution():
    """Carolyn practices the piano for 20 minutes a day and the violin for three times as long. If she practices six days a week, how many minutes does she spend practicing in a month with four weeks?"""
    piano_minutes_per_week = 20 * 6
    violin_minutes_per_week = 3 * piano_minutes_per_week
    total_minutes_per_week = piano_minutes_per_week + violin_minutes_per_week
    total_minutes_per_month = total_minutes_per_week * 4
    result = total_minutes_per_month
    return result

print(solution())