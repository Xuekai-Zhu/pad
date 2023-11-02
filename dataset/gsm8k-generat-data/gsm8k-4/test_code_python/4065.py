def solution():
    """In the spelling bee, Max has 5 points, Dulce has 3 points, and Val has twice the combined points of Max and Dulce. If they are on the same team and their opponents' team has a total of 40 points, how many points are their team behind?"""
    # Calculate the combined points of Max and Dulce
    max_dulce_points = 5 + 3

    # Calculate Val's points
    val_points = max_dulce_points * 2

    # Calculate the total points of their team
    team_points = max_dulce_points + val_points

    # Calculate the points their team is behind
    points_behind = 40 - team_points

    # return the result
    result = points_behind
    return result

print(solution())