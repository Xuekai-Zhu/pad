def solution():
    """Martha has been collecting shells since she turned 5 years old, every month she collects one shell. By her 10th birthday, how many shells will Martha have collected?"""
    years_collecting = 10 - 5
    months_collecting = years_collecting * 12
    shells_per_month = 1
    total_shells = months_collecting * shells_per_month
    result = total_shells
    return result

print(solution())