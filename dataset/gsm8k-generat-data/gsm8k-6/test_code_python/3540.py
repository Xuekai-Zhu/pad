def solution():
    # Calculate the total number of home runs scored by the Cubs and the Cardinals
    cubs_home_runs = 2 + 1 + 2  # Cubs scored 2 home runs in the third inning, 1 home run in the fifth inning and 2 more home runs in the eighth inning
    cardinals_home_runs = 1 + 1  # Cardinals scored 1 home run in the second inning and 1 home run in the fifth inning

    # Calculate the difference in the number of home runs scored by the Cubs and the Cardinals
    difference = cubs_home_runs - cardinals_home_runs
    result = difference
    return result

print(solution())