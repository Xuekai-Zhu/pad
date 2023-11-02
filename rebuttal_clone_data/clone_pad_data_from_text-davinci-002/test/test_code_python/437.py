def solution():
    yards_of_ribbon = 18
    number_of_gifts = 6
    yards_per_gift = 2
    total_yards_used = number_of_gifts * yards_per_gift
    yards_left = yards_of_ribbon - total_yards_used
    result = yards_left
    
    return result

print(solution())