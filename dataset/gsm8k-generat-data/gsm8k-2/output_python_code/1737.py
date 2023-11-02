def solution():
    """Steve has decided to become a baker. On Mondays, Wednesdays and Fridays, he bakes apple pies. On Tuesdays and Thursdays, he bakes cherry pies. If he bakes 12 pies per day, how many more apple pies does he bake than cherry pies in one week?"""
    apple_pies_per_day = 4
    cherry_pies_per_day = 2
    days_per_week = 7
    total_apple_pies = apple_pies_per_day * 3 * days_per_week
    total_cherry_pies = cherry_pies_per_day * 2 * days_per_week
    apple_pie_difference = total_apple_pies - total_cherry_pies
    result = apple_pie_difference
    return result

print(solution())