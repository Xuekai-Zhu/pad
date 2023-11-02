def solution():
    """From Monday to Friday, Elle practices piano for 30 minutes. On Saturday, she practices piano three times as much as on a weekday. There is no practice on Sunday. How many hours does Elle spend practicing piano each week?"""
    weekday_time = 30
    saturday_time = weekday_time * 3
    total_time = (weekday_time * 5) + saturday_time
    result = total_time / 60  # convert to hours
    return result

print(solution())