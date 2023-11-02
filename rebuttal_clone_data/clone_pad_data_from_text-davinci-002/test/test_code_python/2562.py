def solution():
    naps_per_week = 3
    hours_per_nap = 2
    days = 70
    weeks = days / 7
    total_hours = naps_per_week * weeks * hours_per_nap
    result = total_hours
    return result

print(solution())