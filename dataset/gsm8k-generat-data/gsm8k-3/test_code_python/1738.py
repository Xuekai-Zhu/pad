def solution():
    """Steve has decided to become a baker. On Mondays, Wednesdays and Fridays, he bakes apple pies. On Tuesdays and Thursdays, he bakes cherry pies. If he bakes 12 pies per day, how many more apple pies does he bake than cherry pies in one week?"""
    # Define the number of pies Steve bakes per day
    PIES_PER_DAY = 12

    # Calculate the total number of apple pies baked in a week
    apple_pies = 3 * PIES_PER_DAY

    # Calculate the total number of cherry pies baked in a week
    cherry_pies = 2 * PIES_PER_DAY

    # Calculate the difference between the number of apple and cherry pies
    difference = apple_pies - cherry_pies

    # Display the difference
    result = difference
    return result

print(solution())