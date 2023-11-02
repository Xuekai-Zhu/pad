def solution():
    """A high school bowling team's 3 members scored a total of 810 points in their first match. The first bowler scored 1/3 as many points as the second, and the second bowler scored 3 times as high as the third bowler. How many points did the third bowler score?"""
    # Define the total number of points and the relative scores of the bowlers
    total_points = 810
    first_bowler = 1/3
    second_bowler = 1
    third_bowler = 1/3

    # Define the total as a sum of the relative scores of each bowler
    total_score = first_bowler + second_bowler + third_bowler

    # Calculate the score of the third bowler as a fraction of the total score
    third_bowler_fraction = third_bowler / total_score

    # Calculate the points scored by the third bowler
    third_bowler_points = total_points * third_bowler_fraction

    # Return the result
    result = third_bowler_points
    return result

print(solution())