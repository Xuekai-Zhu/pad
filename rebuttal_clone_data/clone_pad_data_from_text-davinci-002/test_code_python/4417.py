def solution():
    total_points = 8 + 12
    levi_points = 8
    brother_points = 12
    goal = 5
    levi_margin = brother_points - levi_points
    levi_needed = goal - levi_margin
    brother_3_points = 3
    levi_total = levi_needed + brother_3_points
    result = levi_total
    return result

print(solution())