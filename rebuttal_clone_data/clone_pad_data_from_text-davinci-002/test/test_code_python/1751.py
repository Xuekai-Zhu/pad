def solution():
    Natasha_minutes_per_day = 30
    Natasha_days_per_week = 7
    Natasha_minutes_per_week = Natasha_minutes_per_day * Natasha_days_per_week
    Natasha_hours_per_week = Natasha_minutes_per_week / 60
    Esteban_minutes_per_day = 10
    Esteban_days_per_week = 9
    Esteban_minutes_per_week = Esteban_minutes_per_day * Esteban_days_per_week
    Esteban_hours_per_week = Esteban_minutes_per_week / 60
    total_hours = Natasha_hours_per_week + Esteban_hours_per_week
    result = total_hours
    return result

print(solution())