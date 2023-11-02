def solution():
    yards_ without_lawnmower = 8
    yards_with_lawnmower = yards_without_lawnmower + (yards_without_lawnmower * 0.5)
    yards_per_week = yards_with_lawnmower * 7
    result = yards_per_week
    return result

print(solution())