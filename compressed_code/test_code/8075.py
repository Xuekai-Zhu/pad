def solution():
    
    minutes_per_brush = 2
    brushes_per_day = 3
    days = 30
    total_minutes = minutes_per_brush * brushes_per_day * days
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())