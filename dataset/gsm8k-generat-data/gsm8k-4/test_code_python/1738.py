def solution():
    """Steve has decided to become a baker. On Mondays, Wednesdays and Fridays, he bakes apple pies. On Tuesdays and Thursdays, he bakes cherry pies. If he bakes 12 pies per day, how many more apple pies does he bake than cherry pies in one week?"""
    # Define the number of pies baked per day
    pies_per_day = 12

    # Calculate the number of apple pies baked in one week
    apple_pies_per_week = 3 * pies_per_day

    # Calculate the number of cherry pies baked in one week
    cherry_pies_per_week = 2 * pies_per_day

    # Calculate the difference in the number of apple pies and cherry pies
    difference = apple_pies_per_week - cherry_pies_per_week

    # return the result
    result = difference
    return result

print(solution())