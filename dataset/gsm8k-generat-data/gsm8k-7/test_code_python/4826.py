def solution():
    points_of_3 = 3
    num_of_3 = 15

    points_of_2 = 2
    num_of_2 = 12

    total_points = 75

    # Calculate the total number of points from scoring 3 points
    total_points_of_3 = points_of_3 * num_of_3

    # Calculate the total number of points from scoring 2 points
    total_points_of_2 = points_of_2 * num_of_2

    # Calculate the total number of points from scoring 1 point
    total_points_of_1 = total_points - total_points_of_3 - total_points_of_2

    result = total_points_of_1
    return result

print(solution())