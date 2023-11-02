def solution():
    """Baseball season opened up with the Chicago Cubs at home at Wrigley Field. They scored 2 home runs in the third inning, 1 home run in the fifth inning and 2 more home runs in the eighth inning. Their opponents, the Cardinals, scored 1 home run in the second inning and 1 home run in the fifth inning. How many more home runs did the Chicago Cubs score than the Cardinals in the game?"""
    # Calculate the total number of home runs scored by the Cubs
    cubs_total_home_runs = 2 + 1 + 2

    # Calculate the total number of home runs scored by the Cardinals
    cardinals_total_home_runs = 1 + 1

    # Calculate the difference in the number of home runs scored
    home_run_difference = cubs_total_home_runs - cardinals_total_home_runs

    # Display the difference in the number of home runs scored
    result = home_run_difference
    return result

print(solution())