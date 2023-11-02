def solution():
    # Calculate the number of apple pies and cherry pies baked in a week
    apple_pies_week = 3 * 12  # Steve bakes 12 apple pies on Mondays, Wednesdays and Fridays
    cherry_pies_week = 2 * 12  # Steve bakes 12 cherry pies on Tuesdays and Thursdays

    # Calculate the difference in the number of apple pies and cherry pies baked in a week
    difference = apple_pies_week - cherry_pies_week
    result = difference
    return result

print(solution())