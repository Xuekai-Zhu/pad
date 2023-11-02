def solution():
    # Calculate the total number of points Liz scores
    liz_points = 5*1 + 3*3 + 4*2  # Liz scores 5 free throws, 3 three-pointers, and 4 two-point jump shots
    opposing_team_points = 10  # the opposing team scores 10 points
    point_difference = 20 - liz_points + opposing_team_points  # calculate the point difference at the end of the game
    result = point_difference
    return result

print(solution())