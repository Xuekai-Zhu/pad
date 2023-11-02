def solution():
    total_weekly_hours = 168
    ugly_betty_hours = 85
    if ugly_betty_hours <= total_weekly_hours:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())