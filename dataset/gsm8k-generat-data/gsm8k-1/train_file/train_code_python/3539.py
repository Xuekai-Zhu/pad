def solution():
    """Baseball season opened up with the Chicago Cubs at home at Wrigley Field. They scored 2 home runs in the third inning, 1 home run in the fifth inning and 2 more home runs in the eighth inning. Their opponents, the Cardinals, scored 1 home run in the second inning and 1 home run in the fifth inning. How many more home runs did the Chicago Cubs score than the Cardinals in the game?"""
    cubs_total_home_runs = 2 + 1 + 2
    cardinals_total_home_runs = 1 + 1
    difference_in_home_runs = cubs_total_home_runs - cardinals_total_home_runs
    result = difference_in_home_runs
    return result

print(solution())