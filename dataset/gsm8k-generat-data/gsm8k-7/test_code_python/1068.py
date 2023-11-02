def solution():
    num_2point_shots = 4
    num_3point_shots = 2
    points_per_2point_shot = 2
    points_per_3point_shot = 3

    # Calculate the total points from 2-point shots
    total_2point_points = num_2point_shots * points_per_2point_shot

    # Calculate the total points from 3-point shots
    total_3point_points = num_3point_shots * points_per_3point_shot

    # Calculate the total points scored in the first quarter
    total_points = total_2point_points + total_3point_points
    result = total_points
    return result

print(solution())