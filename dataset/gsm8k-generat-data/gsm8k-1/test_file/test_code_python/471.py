def solution():
    """It takes 240 minutes of walking to break in a new pair of shoes. Jason wants to try out for the track team in three weeks. If he can walk 4 days a week to break in the new shoes, how long does he have to spend walking each day?"""
    total_minutes = 240
    weeks = 3
    days_per_week = 4
    total_days = weeks * days_per_week
    minutes_per_day = total_minutes / total_days
    result = minutes_per_day
    return result

print(solution())