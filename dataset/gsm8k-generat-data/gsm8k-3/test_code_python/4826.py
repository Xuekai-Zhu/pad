def solution():
    """Tyson played basketball on the schoolyard. He scored three points fifteen times, and two points twelve times. He also scored one point some number of times. How many times did he score one point, if in total he scored 75 points?"""
    # Define the number of times Tyson scored three points and the points for each shot
    three_point_shots = 15
    three_point_score = 3

    # Define the number of times Tyson scored two points and the points for each shot
    two_point_shots = 12
    two_point_score = 2

    # Define the total number of points and the remaining number of shots
    total_points = 75
    remaining_shots = three_point_shots + two_point_shots

    # Calculate the total score and the number of one-point shots
    total_score = three_point_shots * three_point_score + two_point_shots * two_point_score
    one_point_shots = (total_points - total_score) / 1

    # Display the number of one-point shots
    result = one_point_shots
    return result

print(solution())