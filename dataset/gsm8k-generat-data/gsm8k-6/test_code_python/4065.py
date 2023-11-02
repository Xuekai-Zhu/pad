def solution():
    # Calculate the total points of Max and Dulce
    max_and_dulce_points = 5 + 3  

    # Calculate Val's points
    val_points = 2 * max_and_dulce_points  

    # Calculate the total points of their team
    team_points = max_and_dulce_points + val_points  

    # Calculate how many points their team is behind
    points_behind = 40 - team_points  
    result = points_behind
    return result

print(solution())