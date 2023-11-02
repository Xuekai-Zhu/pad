def solution():
    grades_below_B = 4  # Cassidy got four grades below a B
    extra_days = 3 * grades_below_B  # Cassidy gets 3 extra days for each grade below a B
    total_days = 14 + extra_days  # Cassidy is grounded for 14 days for lying about her report card, plus extra days for grades below a B
    result = total_days
    return result

print(solution())