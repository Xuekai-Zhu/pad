def solution():
    """Antonia is trying to improve her health by buying supplements. She has a 7-day pill box she wants to fill. She buys 5 different supplements. 3 of the bottles have 120 pills in them each. 2 of the bottles have 30 pills each. After Antonia has filled her pillbox with one pill of each supplement for 2 weeks, how many pills total does she have left from all 5 bottles?"""
    # Define the number of pills in each bottle
    bottle1 = 120
    bottle2 = 120
    bottle3 = 120
    bottle4 = 30
    bottle5 = 30

    # Calculate the total number of pills in all the bottles
    total_pills = bottle1 + bottle2 + bottle3 + bottle4 + bottle5

    # Calculate the number of pills Antonia takes in two weeks
    pills_per_week = 5 * 7 * 2
    # Since Antonia takes one pill of each supplement per day, she takes a total of 5 pills per day.

    # Calculate the number of pills Antonia has left after two weeks
    pills_left = total_pills - pills_per_week

    # Display the number of pills Antonia has left
    result = pills_left
    return result

print(solution())