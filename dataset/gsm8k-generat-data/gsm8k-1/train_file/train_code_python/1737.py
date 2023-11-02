def solution():
    """Steve has decided to become a baker. On Mondays, Wednesdays and Fridays, he bakes apple pies. On Tuesdays and Thursdays, he bakes cherry pies. If he bakes 12 pies per day, how many more apple pies does he bake than cherry pies in one week?"""
    apple_pies_per_day = 12
    cherry_pies_per_day = 12
    days_per_week = 5
    apple_pies_per_week = apple_pies_per_day * 3
    cherry_pies_per_week = cherry_pies_per_day * 2
    more_apple_pies = apple_pies_per_week - cherry_pies_per_week
    result = more_apple_pies
    return result

print(solution())