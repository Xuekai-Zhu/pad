def solution():
    brewing_time_weeks = 5
    september_days = 30
    september_weeks = september_days / 7
    if september_weeks >= brewing_time_weeks:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())