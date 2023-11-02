def solution():
    num_2point_shots = 7
    num_3point_shots = 3

    # Calculate the total number of points Lemuel made from 2-point shots
    total_points_2point = num_2point_shots * 2

    # Calculate the total number of points Lemuel made from 3-point shots
    total_points_3point = num_3point_shots * 3

    # Calculate the total number of points Lemuel made in the game
    total_points = total_points_2point + total_points_3point
    result = total_points
    return result

print(solution())