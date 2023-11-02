def solution():
    max_points = 5
    dulce_points = 3
    val_points = (max_points + dulce_points) * 2
    opponents_total_points = 40

    # Calculate the total points of Max, Dulce, and Val
    total_points = max_points + dulce_points + val_points

    # Calculate the difference between their team's points and their opponents' points
    difference = opponents_total_points - total_points
    result = difference
    return result

print(solution())