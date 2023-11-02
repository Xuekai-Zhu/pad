def solution():
    """Cassidy is grounded for 14 days for lying about her report card, plus 3 extra days for each grade below a B. If Cassidy got four grades below a B, how long is she grounded for?"""
    grades_below_b = 4
    extra_days = grades_below_b * 3
    total_days = 14 + extra_days
    result = total_days
    return result

print(solution())