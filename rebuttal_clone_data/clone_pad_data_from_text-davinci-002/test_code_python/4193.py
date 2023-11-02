def solution():
    minutes_ironing_shirt = 5
    minutes_ironing_pants = 3
    days_per_week = 5
    weeks = 4
    total_ironing_time = minutes_ironing_shirt + minutes_ironing_pants
    total_minutes = total_ironing_time * days_per_week * weeks
    result = total_minutes
    return result

print(solution())