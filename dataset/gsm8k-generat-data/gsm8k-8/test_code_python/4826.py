def solution():
    # Define the number of points for each type of score
    three_point = 3
    two_point = 2
    one_point = 1

    # Define the number of times each type of score was made
    three_point_count = 15
    two_point_count = 12

    # Calculate the total number of points from three-point and two-point scores
    total_points = three_point * three_point_count + two_point * two_point_count

    # Calculate the number of one-point scores by subtracting the total points from the given total
    one_point_count = (75 - total_points) / one_point
    result = one_point_count
    return result

print(solution())