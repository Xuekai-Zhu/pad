def solution():
    """Josh has 18 yards of ribbon that is to be used equally to 6 gifts. If each gift will use 2 yards of ribbon, how many yards of ribbon will be left?"""
    total_yards = 18
    gifts = 6
    yards_per_gift = 2
    yards_left = total_yards - (gifts * yards_per_gift)
    result = yards_left
    return result

print(solution())