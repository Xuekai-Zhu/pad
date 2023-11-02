def solution():
    points_needed = 2000
    points_earned = 8 * 100
    points_per_snickers = 25
    snickers_needed = (points_needed - points_earned) / points_per_snickers
    result = snickers_needed
    return result

print(solution())