def solution():
    """In the spelling bee, Max has 5 points, Dulce has 3 points, and Val has twice the combined points of Max and Dulce. If they are on the same team and their opponents' team has a total of 40 points, how many points are their team behind?"""
    max_points = 5
    dulce_points = 3
    combined_points = max_points + dulce_points
    val_points = 2 * combined_points
    total_team_points = max_points + dulce_points + val_points
    opponents_points = 40
    points_behind = opponents_points - total_team_points
    result = points_behind
    return result

print(solution())