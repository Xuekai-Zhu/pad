def solution():
    """From Monday to Friday, Elle practices piano for 30 minutes. On Saturday, she practices piano three times as much as on a weekday. There is no practice on Sunday. How many hours does Elle spend practicing piano each week?"""
    weekday_minutes = 30
    saturday_minutes = weekday_minutes * 3
    total_weekday_minutes = weekday_minutes * 5
    total_saturday_minutes = saturday_minutes
    total_minutes = total_weekday_minutes + total_saturday_minutes
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())