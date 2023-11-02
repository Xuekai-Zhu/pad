def solution():
    """Antonia is trying to improve her health by buying supplements. She has a 7-day pill box she wants to fill. She buys 5 different supplements. 3 of the bottles have 120 pills in them each. 2 of the bottles have 30 pills each. After Antonia has filled her pillbox with one pill of each supplement for 2 weeks, how many pills total does she have left from all 5 bottles?"""
    # Define the number of pills in each bottle
    bottle_pills = [120, 120, 120, 30, 30]

    # Calculate the total number of pills Antonia has
    total_pills = sum(bottle_pills)

    # Calculate the number of pills Antonia uses in one week
    weekly_pills = 5 * 7

    # Calculate the number of pills Antonia uses in two weeks
    biweekly_pills = weekly_pills * 2

    # Calculate the number of pills Antonia has left
    pills_left = total_pills - biweekly_pills

    # Return the result
    result = pills_left
    return result

print(solution())